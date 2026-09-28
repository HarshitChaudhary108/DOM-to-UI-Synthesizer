export default function Testimonials() {
  const testimonials = [
    {
      quote: "Scarily accurate! It described my situation perfectly and gave the clarity I needed during a confusing time in my life.",
      author: 'Ananya R.',
      location: 'Mumbai',
    },
    {
      quote: "The predictions about my love life came true within weeks. I'm honestly amazed at how detailed and personal the reading was.",
      author: 'Rohan M.',
      location: 'Bangalore',
    },
    {
      quote: "The dream interpretation was spot on! I finally understand the recurring symbols I've been seeing for months.",
      author: 'Neha S.',
      location: 'Delhi',
    },
  ];
  return (
    <section className="py-12 bg-[#080625] text-[#ffffff] font-[Inter,ui-serif]">
      <div className="max-w-5xl mx-auto px-4 text-center">
        <h2 className="text-2xl md:text-3xl font-bold mb-2">Real stories from people who found clarity through SoulStarr readings.</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-8">
          {testimonials.map((t, i) => (
            <div key={i} className="bg-[#080625]/60 p-6 rounded-lg shadow-md">
              <p className="italic mb-4">&quot;{t.quote}&quot;</p>
              <p className="font-semibold">{t.author}</p>
              <p className="text-sm">{t.location}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
