document.documentElement.classList.remove("no-js");

// Mobile menu
const btn = document.querySelector(".menu-btn");
const nav = document.getElementById("site-nav");
if (btn && nav) {
  btn.addEventListener("click", () => {
    const open = nav.classList.toggle("open");
    btn.setAttribute("aria-expanded", String(open));
    btn.textContent = open ? "Close" : "Menu";
  });
}

// Scroll reveal
const items = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const io = new IntersectionObserver((entries) => {
    entries.forEach((e) => {
      if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
    });
  }, { rootMargin: "0px 0px -8% 0px" });
  items.forEach((el) => io.observe(el));
} else {
  items.forEach((el) => el.classList.add("in"));
}

// Newsletter: set data-endpoint on the form to a Buttondown / Mailchimp / Formspree
// URL to go live. Until then, the form explains that sign-ups aren't open.
document.querySelectorAll("form.signup").forEach((form) => {
  const note = form.parentElement.querySelector(".form-note");
  form.addEventListener("submit", async (ev) => {
    ev.preventDefault();
    const endpoint = form.dataset.endpoint;
    const email = form.querySelector("input[type=email]");
    if (!email.checkValidity()) { note.textContent = "Please enter a valid email address."; return; }
    if (!endpoint) {
      note.textContent = "Newsletter sign-ups open soon — thank you for your interest!";
      return;
    }
    try {
      const res = await fetch(endpoint, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } });
      note.textContent = res.ok ? "You're on the list. Watch your inbox." : "Something went wrong — please try again.";
      if (res.ok) form.reset();
    } catch {
      note.textContent = "Something went wrong — please try again.";
    }
  });
});

const y = document.getElementById("year");
if (y) y.textContent = new Date().getFullYear();

// Copy-to-clipboard for media kit bios
document.querySelectorAll(".copy-btn").forEach((b) => {
  b.addEventListener("click", async () => {
    const el = document.getElementById(b.dataset.copy);
    const text = el.innerText.trim();
    try {
      await navigator.clipboard.writeText(text);
      b.textContent = "Copied";
    } catch {
      const r = document.createRange(); r.selectNodeContents(el);
      const sel = getSelection(); sel.removeAllRanges(); sel.addRange(r);
      b.textContent = "Selected";
    }
    setTimeout(() => (b.textContent = "Copy"), 1800);
  });
});
