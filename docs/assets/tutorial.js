const progress = document.querySelector("[data-progress]");
const cards = document.querySelectorAll("[data-reveal]");

function updateProgress() {
  if (!progress) return;
  const max = document.documentElement.scrollHeight - window.innerHeight;
  const ratio = max > 0 ? window.scrollY / max : 0;
  progress.style.transform = `scaleX(${Math.min(Math.max(ratio, 0), 1)})`;
}

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) entry.target.classList.add("is-visible");
    });
  },
  { threshold: 0.12 },
);

cards.forEach((card) => observer.observe(card));
window.addEventListener("scroll", updateProgress, { passive: true });
updateProgress();
