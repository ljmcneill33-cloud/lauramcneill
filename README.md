# Laura McNeill — Author Website

Static author site for suspense novelist Laura McNeill (also writing as Lauren Clark).
Dark, editorial design: ink background, brass accents, Cormorant Garamond + Inter.

## Pages
- `index.html` — hero, latest novel, book grid, about teaser, newsletter
- `books.html` — all three suspense novels + Lauren Clark titles, with buy links
- `about.html` — biography and timeline
- `contact.html` — readers, media/speaking, academic inquiries

Shared styles in `assets/style.css`, behavior in `assets/site.js`. No build step.

## Publish with GitHub Pages
Settings → Pages → Source: *Deploy from a branch* → `main` / `(root)`.

## To finish before launch
- **Newsletter:** set `data-endpoint="..."` on each `<form class="signup">` to a
  Buttondown / Mailchimp / Formspree URL. Until then the form shows a "sign-ups open soon" note.
- **Book covers:** covers are drawn in CSS. To use real cover art, replace a
  `<div class="cover ...">` block with `<img src="assets/covers/…jpg" alt="…">`.
- **Author photo:** replace the `.portrait` monogram block with an `<img>`.
- **Contact:** add a public contact email or form for book clubs and media.
- **Lauren Clark blurbs** on `books.html` are short placeholders — swap in final copy.
