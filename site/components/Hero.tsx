export default function Hero() {
  return (
    <section className="relative bg-[#080625] text-[#FFFFFF] font-[Inter,sans-serif]">
      <img
        src="https://www.soulstarr.in/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fhero-bg-2026-06-13.0fiz2hbcmi7a4.webp&w=1920&q=80"
        alt="Hero background"
        className="absolute inset-0 w-full h-full object-cover opacity-30"
      />
      <div className="relative max-w-4xl mx-auto px-4 py-24 text-center">
        <h1 className="text-4xl sm:text-5xl md:text-6xl font-bold mb-6 whitespace-pre-line">
          Discover What\nLove Signs\nAre Trying To\nTell You
        </h1>
        <p className="text-lg md:text-xl mb-8 whitespace-pre-line">
          Find clarity in your love life, dreams, and future through personalized spiritual guidance.
        </p>
        <div className="flex flex-col sm:flex-row justify-center gap-4">
          <a
            href="#"
            className="bg-[#D9A56C] text-[#080625] font-medium py-3 px-6 rounded hover:bg-[#c08a52]"
          >
            ❤️\nDoes He/She Love Me?\n\nGet Instant Love Answers\n\n1ST CALL JUST\n₹199\n₹1
          </a>
          <a
            href="#"
            className="bg-[#E8E8E8] text-[#080625] font-medium py-3 px-6 rounded hover:bg-[#d0d0d0]"
          >
            🔮\nGet Free Spiritual Guidance\n\nPast Life • Dream Meaning • Angel Numbers\n\nFREE
          </a>
        </div>
      </div>
    </section>
  );
}
