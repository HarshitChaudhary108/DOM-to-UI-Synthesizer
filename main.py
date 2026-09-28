import subprocess
import sys

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

from agent.graph.agent_graph import build_graph


def run(graph, state: dict) -> dict:
    """Stream node-by-node progress (great for the demo video) and merge updates into state."""
    for chunk in graph.stream(state, stream_mode="updates"):
        for node, update in chunk.items():
            print(f"▶ {node}")
            state = {**state, **update}
    return state


def start_preview() -> subprocess.Popen:
    return subprocess.Popen("npm run dev", cwd="site", shell=True)


def stop(proc: subprocess.Popen) -> None:
    if sys.platform == "win32":
        subprocess.run(f"taskkill /F /T /PID {proc.pid}", shell=True, capture_output=True)
    else:
        proc.terminate()


def main():
    graph = build_graph()
    url = input("Website URL: ").strip()

    state = run(graph, {"mode": "clone", "url": url})
    if not state.get("build_ok"):
        print("\nBuild still failing after retries. Last error:\n", state.get("build_log"))
        return

    dev = start_preview()
    print("\n✅ Preview running at http://localhost:3000  (open DevTools → mobile view for responsive demo)")
    print("Type a change (e.g. 'make the navbar sticky'), or 'exit'.\n")

    try:
        while True:
            instruction = input("modify> ").strip()
            if instruction.lower() in {"exit", "quit"}:
                break
            if not instruction:
                continue
            state = run(graph, {**state, "mode": "modify", "instruction": instruction})
            print("✅ updated (hot reload)" if state.get("build_ok") else f"❌ build failed:\n{state.get('build_log')}")
    finally:
        stop(dev)


if __name__ == "__main__":
    main()