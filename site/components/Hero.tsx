export default function Hero() {
  return (
    <section className="relative w-full min-h-[80vh] flex items-center justify-center text-center bg-[#080625] text-[#ffffff] font-[Inter,ui-serif]">
      <img
        src="https://www.soulstarr.in/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fhero-bg-2026-06-13.0fiz2hbcmi7a4.webp&w=1920&q=80"
        alt="Hero background"
        className="absolute inset-0 w-full h-full object-cover opacity-50"
      />
      <div className="relative z-10 max-w-2xl px-4">
        <h1 className="text-3xl md:text-5xl font-bold mb-4 text-[#87CEEB]">Discover What Love Signs Are Trying To Tell You</h1>
        <p className="mb-8 text-lg md:text-xl">Find clarity in your love life, dreams, and future through personalized spiritual guidance.</p>
        <div className="flex flex-col space-y-4 items-center">
          <button className="bg-[#9d3f3f] hover:bg-[#9d3f3f]/90 text-[#ffffff] font-medium py-3 px-6 rounded transition">
            ❤️ Does He/She Love Me?&#10;Get Instant Love Answers&#10;1ST CALL JUST &#8377;199&#10;&#8377;1
          </button>
          <button className="bg-[#4c4c4c] hover:bg-[#4c4c4c]/90 text-[#ffffff] font-medium py-3 px-6 rounded transition">
            🔮 Get Free Spiritual Guidance&#10;Past Life • Dream Meaning • Angel Numbers&#10;FREE
          </button>
        </div>
      </div>
    </section>
  );
}
