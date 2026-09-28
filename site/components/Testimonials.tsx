export default function Testimonials() {
  const quotes = [
    {
      text: "\u201cScarily accurate! It described my situation perfectly and gave the clarity I needed during a confusing time in my life.\u201d",
      author: "Ananya R.",
      location: "Mumbai"
    },
    {
      text: "\u201cThe predictions about my love life came true within weeks. I'm honestly amazed at how detailed and personal the reading was.\u201d",
      author: "Rohan M.",
      location: "Bangalore"
    },
    {
      text: "\u201cThe dream interpretation was spot on! I finally understand the recurring symbols I've been seeing for months.\u201d",
      author: "Neha S.",
      location: "Delhi"
    }
  ];
  return (
    <section className="bg-[#080625] text-[#FFFFFF] py-16 font-[Inter,sans-serif]">
      <div className="max-w-4xl mx-auto px-4 text-center">
        <h2 className="text-3xl font-bold mb-4 whitespace-pre-line">✶ Real Stories ✶</h2>
        <p className="mb-12 whitespace-pre-line">Real stories from people who found clarity through SoulStarr readings.</p>
        <div className="space-y-8">
          {quotes.map((q, i) => (
            <blockquote key={i} className="border-l-4 border-[#D9A56C] pl-4 text-left">
              <p className="italic mb-2">{q.text}</p>
              <footer className="text-sm">
                — {q.author}, {q.location}
              </footer>
            </blockquote>
          ))}
        </div>
      </div>
    </section>
  );
}
