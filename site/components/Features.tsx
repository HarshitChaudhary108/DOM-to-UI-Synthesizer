export default function Features() {
  const cards = [
    'Love & Relationships',
    'Past Life',
    'Dream Meaning',
    'Angel Numbers',
  ];
  return (
    <section className="py-12 bg-[#080625] text-[#ffffff] font-[Inter,ui-serif]">
      <div className="max-w-5xl mx-auto px-4 text-center">
        <h2 className="text-2xl md:text-3xl font-bold mb-2">Love & Relationships</h2>
        <p className="mb-8">Love, soulmates & relationship guidance.</p>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          {cards.map((title) => (
            <div key={title} className="bg-[#080625]/60 p-6 rounded-lg hover:bg-[#080625]/80 transition">
              <h3 className="text-xl font-semibold mb-2">{title}</h3>
              <button className="mt-4 inline-block bg-[#9d3f3f] hover:bg-[#9d3f3f]/90 text-[#ffffff] px-4 py-2 rounded">
                Explore
              </button>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
