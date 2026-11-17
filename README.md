# Laura McNeill — Author Website

Static author site for suspense novelist Laura McNeill (also writing as Lauren Clark).
Dark, editorial design: ink background, brass accents, Cormorant Garamond + Inter.

## Pages
- `index.html` — hero, latest novel, book grid, about teaser, newsletter
- `books.html` — all three suspense novels + Lauren Clark titles, with buy links
- `about.html` — biography and timeline
- `consulting.html` — professional landing: hero, free-guide signup, why work with Laura, six services, audiences, process, book-a-call
- `speaking.html` — Training & Speaking: keynotes, workshops, full-day institute, author events
- `media.html` — milestones & press, media kit (copyable bios), fast facts, interview topics, speaker intro
- `ai-questions.html` — free guide: 10 Questions to Ask Before Bringing AI Into Your Course (printable)

The author pages (Home, Books, About, Contact) use the dark theme in `assets/style.css`.
The professional pages also load `assets/pro.css`, a bright navy/blue theme (Lora + Montserrat).
Which pages use it is set by the `PRO` list in `tools/build.py`.
- `contact.html` — readers, media/speaking, academic inquiries

Shared styles in `assets/style.css`, behavior in `assets/site.js`. No build step is needed to serve the site.

Pages are generated from `tools/build.py` (shared header/footer). After editing page content there, run `python3 tools/build.py` to regenerate the HTML.

## Publish with GitHub Pages
Settings → Pages → Source: *Deploy from a branch* → `main` / `(root)`.

## To finish before launch
- **Newsletter & guide signup:** set `data-endpoint="..."` on each `<form class="signup">` / `<form class="magnet-form">` to a
  Buttondown / Mailchimp / Formspree URL. Until then the form shows a "sign-ups open soon" note.
- **Book covers:** covers are drawn in CSS. To use real cover art, replace a
  `<div class="cover ...">` block with `<img src="assets/covers/…jpg" alt="…">`.
- **Author photo:** replace the `.portrait` monogram block with an `<img>`.
- **Contact:** add a public contact email or form for book clubs and media.
- **Consulting:** add a booking link (e.g. Calendly) or inquiry form to the "Have a project in mind?" section; adjust services/FAQ to your actual offerings.
- **Media kit:** add a downloadable headshot and cover images; review the bios and speaker intro.
- **Lauren Clark blurbs** on `books.html` are short placeholders — swap in final copy.
