import os, sys
# Regenerate all pages:  python3 tools/build.py .
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..")

MOTIFS = {
 "gravity": '<svg class="motif" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width=".8"><circle cx="50" cy="50" r="44"/><circle cx="50" cy="50" r="30"/><circle cx="50" cy="50" r="16"/><circle cx="50" cy="50" r="3" fill="currentColor"/><path d="M50 2v96M2 50h96"/></svg>',
 "sister": '<svg class="motif" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width=".8"><rect x="14" y="8" width="72" height="84"/><path d="M26 8v84M38 8v84M50 8v84M62 8v84M74 8v84"/><circle cx="50" cy="50" r="9"/></svg>',
 "breaks": '<svg class="motif" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width=".8"><circle cx="50" cy="50" r="44"/><path d="M50 6 44 30l12 10-14 16 10 12-8 26"/><path d="M56 40l20-8M42 56 18 62M52 68l22 10"/></svg>',
 "dixie": '<svg class="motif" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width=".8"><path d="M50 10c10 18 30 22 30 42a30 30 0 0 1-60 0c0-20 20-24 30-42Z"/><path d="M50 30v62"/></svg>',
 "stardust": '<svg class="motif" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width=".8"><path d="M50 8l6 36 36 6-36 6-6 36-6-36-36-6 36-6Z"/><circle cx="20" cy="22" r="1.5" fill="currentColor"/><circle cx="82" cy="78" r="1.5" fill="currentColor"/><circle cx="80" cy="20" r="1" fill="currentColor"/></svg>',
 "pie": '<svg class="motif" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width=".8"><circle cx="50" cy="50" r="40"/><circle cx="50" cy="50" r="32"/><path d="M50 18v64M18 50h64M27 27l46 46M73 27 27 73"/></svg>',
 "tuned": '<svg class="motif" viewBox="0 0 100 100" fill="none" stroke="currentColor" stroke-width=".8"><rect x="10" y="22" width="80" height="58" rx="4"/><path d="M38 22 26 6M62 22l12-16M10 64h80"/><circle cx="50" cy="43" r="10"/></svg>',
}

def cover(key, title, author="Laura McNeill", kicker="A Novel"):
    return f'''<div class="cover {key}" role="img" aria-label="{title} by {author}">
  <span class="c-author">{author}</span>
  {MOTIFS[key]}
  <span class="c-title">{title}</span>
  <span class="c-kicker">{kicker}</span>
</div>'''

def buy(title, author="Laura McNeill"):
    q = (title + " " + author).replace(" ", "+")
    return f'''<div class="btn-row">
  <a class="btn" href="https://bookshop.org/search?keywords={q}" rel="noopener" target="_blank">Bookshop.org</a>
  <a class="btn ghost" href="https://www.amazon.com/s?k={q}" rel="noopener" target="_blank">Amazon</a>
  <a class="btn ghost" href="https://www.barnesandnoble.com/s/{q}" rel="noopener" target="_blank">Barnes &amp; Noble</a>
</div>'''

NAV = [("index.html", "Home"), ("books.html", "Books"), ("about.html", "About"), ("consulting.html", "Consulting"), ("speaking.html", "Training &amp; Speaking"), ("media.html", "Media"), ("contact.html", "Contact")]

PRO = {"consulting.html", "speaking.html", "media.html", "ai-questions.html"}

def page(fname, title, desc, body):
    pro = fname in PRO
    nav = "\n".join(
        f'<a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a>' for h, t in NAV)
    return f'''<!doctype html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta name="theme-color" content="{"#1e3d58" if pro else "#0d0f14"}">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@400;500;600{"&family=Lora:ital,wght@0,500;0,600;0,700;1,500&family=Montserrat:wght@400;500;600" if pro else ""}&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">{chr(10) + '<link rel="stylesheet" href="assets/pro.css">' if pro else ""}
</head>
<body{' class="pro"' if pro else ""}>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="wordmark" href="index.html">Laura <span>McNeill</span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main">
{nav}
    </nav>
{'    <a class="nav-cta" href="contact.html">Contact Laura</a>' + chr(10) if pro else ""}  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div>
        <a class="wordmark" href="index.html">Laura <span>McNeill</span></a>
        <p style="margin-top:16px">Suspense novelist, former TV news anchor, and professor of instructional technology. Also writing women&rsquo;s fiction as Lauren Clark.</p>
      </div>
      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="books.html">Books</a></li>
          <li><a href="books.html#lauren-clark">Writing as Lauren Clark</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="consulting.html">Consulting</a></li>
          <li><a href="speaking.html">Speaking</a></li>
          <li><a href="media.html">Media &amp; Press</a></li>
          <li><a href="ai-questions.html">Free AI guide</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Elsewhere</h4>
        <ul>
          <li><a href="https://www.goodreads.com/author/show/5280308.Laura_McNeill" rel="noopener" target="_blank">Goodreads</a></li>
          <li><a href="https://sites.ua.edu/lmcneill" rel="noopener" target="_blank">Faculty page</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="year">2026</span> Laura McNeill. All rights reserved.</span>
      <span>Alabama &middot; Gulf Coast</span>
    </div>
  </div>
</footer>
<script src="assets/site.js"></script>
</body>
</html>
'''

NEWSLETTER = '''<section class="newsletter section-alt" id="newsletter">
  <div class="wrap reveal">
    <p class="eyebrow">The Newsletter</p>
    <h2>Secrets, delivered.</h2>
    <p>News on upcoming books, behind-the-scenes notes from the writing desk, and the occasional story from the newsroom days. No spam &mdash; just the good stuff.</p>
    <form class="signup" data-endpoint="" novalidate>
      <label for="nl-email" class="skip">Email address</label>
      <input id="nl-email" type="email" name="email" placeholder="Your email address" required autocomplete="email">
      <button class="btn" type="submit">Subscribe</button>
    </form>
    <p class="form-note" role="status" aria-live="polite"></p>
  </div>
</section>'''

# ---------------- HOME ----------------
home = f'''
<section class="hero">
  <div class="wrap">
    <div class="reveal">
      <p class="eyebrow">Suspense from the Alabama Gulf Coast</p>
      <h1>Every family keeps <em>secrets.</em><br>Some of them pull you under.</h1>
      <p class="lede">Laura McNeill writes psychological suspense about mothers, sisters and daughters caught in the undertow of the lies closest to home.</p>
      <div class="btn-row">
        <a class="btn" href="books.html">Explore the Books</a>
        <a class="btn ghost" href="about.html">Meet Laura</a>
      </div>
    </div>
    <a class="hero-cover reveal" href="books.html#the-world-breaks-everyone" aria-label="The World Breaks Everyone — read more">
      {cover("breaks", "The World Breaks Everyone")}
    </a>
  </div>
</section>

<section class="section-alt">
  <div class="wrap split">
    <div class="reveal">{cover("breaks", "The World Breaks Everyone")}</div>
    <div class="reveal">
      <p class="eyebrow">Latest Novel</p>
      <h2>The World Breaks Everyone</h2>
      <p class="quote">Sixteen, alone, and running out of places to hide.</p>
      <p>Olivia is carrying more than any sixteen-year-old should: guilt over her mother&rsquo;s death, a father who has vanished, and the growing certainty that someone is coming for her. As the danger closes in, it threatens not only Olivia but everyone she lets close.</p>
      <div class="btn-row">
        <a class="btn" href="books.html#the-world-breaks-everyone">Read More</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <div><p class="eyebrow">The Novels</p><h2>Books by Laura McNeill</h2></div>
      <a class="more" href="books.html">All books &rarr;</a>
    </div>
    <div class="book-grid">
      <a class="book-card reveal" href="books.html#center-of-gravity">{cover("gravity", "Center of Gravity")}<h3>Center of Gravity</h3><span class="meta">2015 &middot; Debut</span></a>
      <a class="book-card reveal" href="books.html#sister-dear">{cover("sister", "Sister Dear")}<h3>Sister Dear</h3><span class="meta">2016</span></a>
      <a class="book-card reveal" href="books.html#the-world-breaks-everyone">{cover("breaks", "The World Breaks Everyone")}<h3>The World Breaks Everyone</h3><span class="meta">2018</span></a>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="wrap split reverse">
    <div class="reveal">
      <div class="portrait"><span class="mono">L<i>M</i></span><span class="cap">Author &middot; Anchor &middot; Professor</span></div>
    </div>
    <div class="reveal">
      <p class="eyebrow">About Laura</p>
      <h2>From the anchor desk to the dark side of the Gulf Coast.</h2>
      <p>Before she wrote suspense, Laura McNeill spent six years behind the anchor desk at two CBS affiliates, earning awards from the Associated Press. She traded breaking news for the Alabama Gulf Coast, a family, and the stories that wouldn&rsquo;t leave her alone.</p>
      <p>Today she writes novels, teaches as a professor of instructional technology at The University of Alabama, and pens women&rsquo;s fiction under the name Lauren Clark.</p>
      <div class="btn-row"><a class="btn ghost" href="about.html">Full Biography</a></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal">
      <div><p class="eyebrow">Work with Laura</p><h2>Ways to connect</h2></div>
    </div>
    <div class="paths">
      <a class="path reveal" href="speaking.html"><span class="path-k">Speaking</span><h3>Keynotes &amp; workshops</h3><p>Talks on teaching in the age of AI, engaging course design, and the craft of storytelling &mdash; for campuses, conferences, libraries and book festivals.</p><span class="path-go">Explore talks &rarr;</span></a>
      <a class="path reveal" href="consulting.html"><span class="path-k">Consulting</span><h3>Course design &amp; ed tech</h3><p>Partnering with universities, schools and organizations on course design, faculty development and purposeful technology.</p><span class="path-go">View services &rarr;</span></a>
      <a class="path reveal" href="books.html"><span class="path-k">Books</span><h3>Suspense &amp; women&rsquo;s fiction</h3><p>Three suspense novels as Laura McNeill and award-winning women&rsquo;s fiction as Lauren Clark &mdash; plus book club visits.</p><span class="path-go">Browse books &rarr;</span></a>
    </div>
  </div>
</section>

{NEWSLETTER}
'''

# ---------------- BOOKS ----------------
def detail(anchor, key, title, tagline, facts, paras, author="Laura McNeill", flip=False):
    f = "".join(f"<li><strong>{k}</strong> {v}</li>" for k, v in facts)
    p = "".join(f"<p>{x}</p>" for x in paras)
    return f'''<article class="book-detail" id="{anchor}">
  <div class="wrap split{" reverse" if flip else ""}">
    <div class="reveal">{cover(key, title, author)}</div>
    <div class="reveal">
      <h2>{title}</h2>
      <p class="tagline">{tagline}</p>
      <ul class="facts">{f}</ul>
      {p}
      {buy(title, author)}
    </div>
  </div>
</article>'''

def lc_card(anchor, key, title, line):
    return f'''<div class="book-card reveal" id="{anchor}">{cover(key, title, "Lauren Clark")}<h3>{title}</h3><span class="meta">Women&rsquo;s fiction</span><p style="color:var(--paper-dim);font-size:.95rem;margin-top:10px">{line}</p></div>'''

books = f'''
<header class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Books</p>
    <h1>The Novels</h1>
    <p>Psychological suspense set along the Alabama Gulf Coast, plus lighter, award-winning women&rsquo;s fiction written as Lauren Clark.</p>
    <nav class="tabs" aria-label="Jump to book">
      <a href="#the-world-breaks-everyone">The World Breaks Everyone</a>
      <a href="#sister-dear">Sister Dear</a>
      <a href="#center-of-gravity">Center of Gravity</a>
      <a href="#lauren-clark">As Lauren Clark</a>
    </nav>
  </div>
</header>

{detail("the-world-breaks-everyone", "breaks", "The World Breaks Everyone",
  "Sixteen, alone, and running out of places to hide.",
  [("Published", "2018"), ("Genre", "Suspense")],
  ["Olivia is sixteen and running. She carries the guilt of her mother&rsquo;s death and the ache of a father who has disappeared without a word &mdash; and she is increasingly sure that whatever took them is now coming for her.",
   "Fast-paced and tightly wound, <em>The World Breaks Everyone</em> follows a girl who has learned that the danger isn&rsquo;t only to herself. Everyone she lets in is at risk, too."])}

{detail("sister-dear", "sister", "Sister Dear",
  "Ten years for a crime she didn&rsquo;t commit. Now she&rsquo;s coming home.",
  [("Published", "2016"), ("Publisher", "Thomas Nelson"), ("Genre", "Suspense")],
  ["In 2006, Allie Marshall went to prison for manslaughter in the death of a beloved high school football coach. Ten years later she is paroled &mdash; still insisting she didn&rsquo;t do it &mdash; and determined to rebuild a life with the daughter who was five when she left.",
   "But Caroline is a teenager now, raised by Allie&rsquo;s sister Emma, and the town hasn&rsquo;t forgotten. Told through the eyes of Allie, Emma, Caroline and the local sheriff, <em>Sister Dear</em> is a story of family loyalty, buried truth, and the price of a second chance."],
  flip=True)}

{detail("center-of-gravity", "gravity", "Center of Gravity",
  "A perfect marriage. A web of lies. A mother&rsquo;s fight to hold on.",
  [("Published", "July 2015"), ("Publisher", "Thomas Nelson"), ("Genre", "Debut suspense")],
  ["Ava Carson thought she knew the man she married. But on the Gulf Coast of Alabama, the life she built begins to tilt &mdash; and Ava finds herself ricocheted into a web of secrets and lies that threatens everything she loves, including her children.",
   "Laura McNeill&rsquo;s debut novel is a suspenseful portrait of a marriage unraveling and a mother who refuses to let go."])}

<section class="section-alt" id="lauren-clark">
  <div class="wrap">
    <div class="pen-name-note reveal">
      <p class="eyebrow">Writing as Lauren Clark</p>
      <h2>Women&rsquo;s fiction with a Southern heart</h2>
      <p style="color:var(--paper-dim)">Under the pen name Lauren Clark, Laura writes warm, witty, award-winning novels about friendship, small towns and second chances &mdash; the lighter side of the same Southern world.</p>
    </div>
    <div class="book-grid">
      {lc_card("dancing-naked-in-dixie", "dixie", "Dancing Naked in Dixie", "A big-city travel writer is sent to a small Alabama town &mdash; and finds far more than a story.")}
      {lc_card("stardust-summer", "stardust", "Stardust Summer", "A summer that changes everything, written with Lauren Clark&rsquo;s trademark warmth.")}
      {lc_card("pie-girls", "pie", "Pie Girls", "Small-town life, friendship and fresh starts &mdash; served by the slice.")}
      {lc_card("stay-tuned", "tuned", "Stay Tuned", "Love, ambition and life in front of the camera.")}
    </div>
  </div>
</section>

{NEWSLETTER}
'''

# ---------------- ABOUT ----------------
about = f'''
<header class="page-hero">
  <div class="wrap">
    <p class="eyebrow">About</p>
    <h1>Laura McNeill</h1>
    <p>Novelist. Former award-winning TV news anchor. Professor of instructional technology. Storyteller in every one of those jobs.</p>
  </div>
</header>

<section>
  <div class="wrap split">
    <div class="reveal">
      <div class="portrait"><span class="mono">L<i>M</i></span><span class="cap">Tuscaloosa &middot; Gulf Coast</span></div>
    </div>
    <div class="reveal">
      <p class="eyebrow">Biography</p>
      <h2>A journalist&rsquo;s instinct for the story behind the story.</h2>
      <p>Laura McNeill spent six years behind the anchor desk at two CBS affiliates, where her reporting earned awards from the Associated Press. Years in the newsroom taught her that the most compelling stories are rarely the ones on the surface.</p>
      <p>She moved to the Alabama Gulf Coast to raise her family and write novels. Her debut suspense novel, <a href="books.html#center-of-gravity"><em>Center of Gravity</em></a>, was published by Thomas Nelson, an imprint of HarperCollins, in 2015, followed by <a href="books.html#sister-dear"><em>Sister Dear</em></a> in 2016 and <a href="books.html#the-world-breaks-everyone"><em>The World Breaks Everyone</em></a> in 2018.</p>
      <p>Writing as <a href="books.html#lauren-clark">Lauren Clark</a>, she is also the author of award-winning women&rsquo;s fiction, including <em>Dancing Naked in Dixie</em>, <em>Stardust Summer</em>, <em>Pie Girls</em> and <em>Stay Tuned</em>.</p>
      <p>Today Laura is a professor of instructional technology at The University of Alabama, where she also serves as an instructional consultant for the university&rsquo;s Teaching Academy &mdash; helping faculty tell better stories in the classroom.</p>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Along the Way</p>
      <h2>A life in stories</h2>
      <p style="color:var(--paper-dim)">From newsroom deadlines to novel drafts to the university classroom.</p>
    </div>
    <ol class="timeline reveal">
      <li><span class="when">Newsroom years</span><h3>Anchor &amp; reporter</h3><p>Six years on air at two CBS affiliates; honored by the Associated Press.</p></li>
      <li><span class="when">2001</span><h3>M.A., Journalism &amp; Public Relations</h3><p>Graduate study that sharpened a reporter&rsquo;s craft.</p></li>
      <li><span class="when">2015</span><h3><em>Center of Gravity</em></h3><p>Debut suspense novel. The same year: an M.S. in Interactive Technology.</p></li>
      <li><span class="when">2016</span><h3><em>Sister Dear</em></h3><p>Second novel with Thomas Nelson.</p></li>
      <li><span class="when">2018</span><h3><em>The World Breaks Everyone</em></h3><p>Her third suspense novel.</p></li>
      <li><span class="when">2019</span><h3>Ph.D., The University of Alabama</h3><p>Instructional Leadership, with a concentration in Instructional Technology.</p></li>
      <li><span class="when">2021 &ndash; Now</span><h3>Professor</h3><p>Teaching instructional technology at The University of Alabama.</p></li>
    </ol>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="pillars reveal">
      <div class="pillar"><div class="num">I.</div><h3>The reporter</h3><p>Deadline discipline and an ear for what people don&rsquo;t say on camera.</p></div>
      <div class="pillar"><div class="num">II.</div><h3>The novelist</h3><p>Suspense rooted in family, loyalty and the lies we tell to protect the people we love.</p></div>
      <div class="pillar"><div class="num">III.</div><h3>The teacher</h3><p>Research and teaching on how technology and storytelling shape the way we learn.</p></div>
    </div>
  </div>
</section>

{NEWSLETTER}
'''

# ---------------- CONTACT ----------------
contact = f'''
<header class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Contact</p>
    <h1>Get in touch</h1>
    <p>For book clubs, events, media and speaking requests, here&rsquo;s where to find Laura.</p>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="contact-grid reveal">
      <div class="contact-card">
        <p class="eyebrow">Readers &amp; Book Clubs</p>
        <h3>Book club visits</h3>
        <p>Laura loves talking with readers, in person or virtually. Reading <em>Sister Dear</em> or <em>Center of Gravity</em> with your group? Reach out to arrange a visit.</p>
      </div>
      <div class="contact-card">
        <p class="eyebrow">Media &amp; Speaking</p>
        <h3>Interviews &amp; events</h3>
        <p>A former TV anchor at home in front of a microphone, Laura speaks on writing suspense, journalism, and technology in teaching and learning. See <a href=\"consulting.html\">consulting &amp; speaking</a>.</p>
      </div>
      <div class="contact-card">
        <p class="eyebrow">Academic</p>
        <h3>University inquiries</h3>
        <p>For research, teaching and instructional technology inquiries, visit Laura&rsquo;s faculty page at The University of Alabama.</p>
        <p><a href="https://sites.ua.edu/lmcneill" rel="noopener" target="_blank">sites.ua.edu/lmcneill &rarr;</a></p>
      </div>
    </div>
  </div>
</section>

{NEWSLETTER}
'''


# ---------------- PROFESSIONAL PAGES (light "pro" theme) ----------------
ICONS = {
 "design": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="4" width="18" height="14" rx="2"/><path d="M8 21h8M12 18v3M7 9h6M7 13h10"/></svg>',
 "people": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-3.3 2.7-6 6-6s6 2.7 6 6M15 20c0-2.2 1-4 3-4.6"/></svg>',
 "ai": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="6" y="6" width="12" height="12" rx="2"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/><path d="M10 10h4v4h-4z"/></svg>',
 "mic": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="9" y="2" width="6" height="12" rx="3"/><path d="M5 11a7 7 0 0 0 14 0M12 18v4M8 22h8"/></svg>',
 "video": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2" y="6" width="14" height="12" rx="2"/><path d="m16 10 6-3v10l-6-3"/></svg>',
 "compass": '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5z"/></svg>',
}

def svc_card(icon, title, text):
    return f'<article class="svc reveal"><div class="ico">{ICONS[icon]}</div><h3>{title}</h3><p>{text}</p></article>'

BLOB = '<div class="blob"><span class="mono">L<i>M</i></span><span class="cap">Dr. Laura McNeill</span></div>'

GUIDE_TEASER = """<section class="band-blue on-dark magnet" id="guide">
  <div class="wrap reveal">
    <h2>10 Questions to Ask Before Bringing AI Into Your Course</h2>
    <div class="stack">
      <p>AI tools are arriving faster than syllabi can change.</p>
      <p>Students are using them. Colleagues are experimenting. Administrators are asking.</p>
      <p>But adoption without intention puts learning at risk.</p>
    </div>
    <p style="margin-top:1.2em">Before you redesign, ban, or embrace, work through <em>10 Questions to Ask Before Bringing AI Into Your Course</em> &mdash; a free guide for faculty and instructional leaders.</p>
    <div class="btn-row" style="justify-content:center"><a class="btn" href="ai-questions.html">Read the free guide</a></div>
    <form class="magnet-form" data-endpoint="" novalidate>
      <p style="grid-column:1/-1;margin:0;font-weight:600">Prefer it in your inbox? Share your name and email.</p>
      <label class="skip" for="g-first">First name</label><input id="g-first" name="first_name" placeholder="First Name" autocomplete="given-name">
      <label class="skip" for="g-last">Last name</label><input id="g-last" name="last_name" placeholder="Last Name" autocomplete="family-name">
      <label class="skip" for="g-email">Email</label><input id="g-email" type="email" name="email" placeholder="Email Address" required autocomplete="email">
      <button class="btn" type="submit">Send me the questions</button>
    </form>
    <p class="form-note" role="status" aria-live="polite"></p>
  </div>
</section>"""

consulting = f"""
<section class="pro-hero on-dark">
  <div class="wrap">
    <div class="reveal">
      <p class="eyebrow">Dr. Laura McNeill &middot; Consulting</p>
      <h1>Teaching with Intention.</h1>
      <p class="sub">Technology with Purpose.</p>
      <p class="lede">Course design, faculty development and AI strategy for colleges, schools and organizations &mdash; grounded in research, built for real classrooms.</p>
      <div class="btn-row">
        <a class="btn" href="#services">Discover services</a>
        <a class="btn ghost" href="ai-questions.html">Get the free guide</a>
      </div>
    </div>
    <div class="reveal">{BLOB}</div>
  </div>
</section>

{GUIDE_TEASER}

<section>
  <div class="wrap split">
    <div class="reveal">{BLOB}</div>
    <div class="reveal">
      <h2 style="color:var(--blue)">Why work with Laura?</h2>
      <p style="font-size:1.2rem;color:var(--navy)">Because good teaching is a story well told &mdash; and technology should help tell it, not get in the way.</p>
      <p>Laura has spent her career helping people understand complicated things. Six years as an award-winning television anchor taught her to make information clear under pressure. A Ph.D. in instructional technology and years as an instructional consultant for The University of Alabama&rsquo;s Teaching Academy taught her how people actually learn.</p>
      <p>That combination shapes every engagement: practical, evidence-based and human-centered. Laura helps faculty and leaders see past the hype, focus on learners, and choose the tools and designs that genuinely serve them.</p>
      <p>She brings the same curiosity to every project that she brings to her novels &mdash; always asking what&rsquo;s really going on beneath the surface.</p>
    </div>
  </div>
</section>

<section class="section-alt" id="services" style="scroll-margin-top:72px">
  <div class="wrap">
    <div class="reveal" style="text-align:center;max-width:760px;margin:0 auto 48px">
      <h2>Services</h2>
      <p style="color:var(--paper-dim)">From AI readiness to course redesign, Laura partners with institutions to teach with purpose and adapt with confidence. Ready to move from ideas to impact?</p>
      <div class="btn-row" style="justify-content:center"><a class="btn" href="media.html">Get the speaker kit</a></div>
    </div>
    <div class="svc-grid">
      {svc_card("ai", "AI Strategy for Teaching &amp; Learning", "I help departments and teaching centers move beyond scattered experiments &mdash; aligning course policies, assignment design and faculty guidance so AI supports learning instead of short-circuiting it.")}
      {svc_card("design", "Course &amp; Program Design", "I help instructors and programs build online, hybrid and face-to-face courses with clear outcomes, aligned assessments and accessible materials &mdash; so learners know where they&rsquo;re going and how to get there.")}
      {svc_card("people", "Faculty Development &amp; Workshops", "I design and lead interactive workshops, institutes and one-on-one consultations that leave instructors with strategies they can use the next time they teach.")}
      {svc_card("mic", "Keynote &amp; Conference Speaking", "I deliver keynotes built for your audience and your moment &mdash; moving people from uncertainty to understanding, with a broadcaster&rsquo;s sense of timing.")}
      {svc_card("video", "Media &amp; On-Camera Coaching", "I help educators and leaders present with confidence on camera and on stage, drawing on six years behind the anchor desk &mdash; from recorded lectures to live interviews.")}
      {svc_card("compass", "Custom Projects &amp; Support", "For needs that don&rsquo;t fit a single category &mdash; a stalled course launch, a new program, a technology rollout &mdash; I provide tailored support to get the work moving.")}
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="reveal">
      <h2>Who I work with</h2>
      <p style="color:var(--paper-dim)">Engagements are shaped around your people, your timeline and your goals &mdash; from a single keynote to a semester-long redesign.</p>
    </div>
    <ul class="audience reveal">
      <li><strong>Colleges &amp; universities</strong><span>Teaching centers, online learning offices, departments and faculty cohorts.</span></li>
      <li><strong>K&ndash;12 schools &amp; districts</strong><span>Technology integration and professional learning for teachers and leaders.</span></li>
      <li><strong>Organizations &amp; nonprofits</strong><span>Training design, onboarding and learning content for adult learners.</span></li>
      <li><strong>Professional associations</strong><span>Conference keynotes, workshops and member education.</span></li>
    </ul>
  </div>
</section>

<section class="section-alt">
  <div class="wrap">
    <h2 class="reveal" style="text-align:center;margin-bottom:48px">How an engagement works</h2>
    <ol class="steps reveal">
      <li><span class="step-n">1</span><h3>Listen</h3><p>A free 30-minute call to understand your learners, challenges and goals.</p></li>
      <li><span class="step-n">2</span><h3>Plan</h3><p>A clear proposal with scope, deliverables and timeline &mdash; no surprises.</p></li>
      <li><span class="step-n">3</span><h3>Build</h3><p>Collaborative design and delivery, with regular check-ins.</p></li>
      <li><span class="step-n">4</span><h3>Sustain</h3><p>Resources and follow-up so the work continues after we finish.</p></li>
    </ol>
  </div>
</section>

<section class="cta-band on-dark" id="start" style="scroll-margin-top:72px">
  <div class="wrap reveal">
    <h2>Ready to explore how I can support your team?</h2>
    <p>Schedule a free 30-minute consultation to talk through your goals, your learners and your timeline.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="contact.html">Book a call</a>
      <a class="btn ghost" href="speaking.html">Training &amp; speaking</a>
    </div>
  </div>
</section>
"""

def offer_item(title, length, who, text):
    l = f"<small>({length})</small>" if length else ""
    return f'<li><span class="t">&ldquo;{title}&rdquo;{l}</span><span class="for">For {who}</span><p>{text}</p></li>'

speaking = f"""
<section class="pro-hero on-dark solo">
  <div class="wrap reveal">
    <h1>Training &amp; Speaking</h1>
    <p class="lede">Laura works with educators and leaders who want to use technology well &mdash; not just adopt it. Sessions are practical, grounded in real classrooms, and designed to build both skill and judgment. Available in person or virtually, and customized for every audience.</p>
    <div class="btn-row"><a class="btn" href="media.html">Get the speaker kit</a><a class="btn ghost" href="#book">Check availability</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="offer reveal">
      <div class="offer-side">
        <h2>Keynotes</h2>
        <p>45&ndash;60 minute talks for conferences, convocations and kickoffs &mdash; delivered with a former anchor&rsquo;s presence and an educator&rsquo;s substance.</p>
        <p class="price">Virtual or in person &middot; connect for pricing</p>
        <a class="btn" href="contact.html">Host a keynote</a>
      </div>
      <ul class="offer-list">
        {offer_item("Teaching in the Age of AI", "", "faculty, academic leaders and teaching centers", "A clear-eyed look at what generative AI changes about learning, assessment and integrity &mdash; and what stays the same &mdash; with strategies faculty can use immediately.")}
        {offer_item("Designing for Engagement", "", "broad education audiences", "Evidence-based ways to build online, hybrid and face-to-face courses that hold attention and that learners actually finish.")}
        {offer_item("From the Anchor Desk: Communicating with Confidence", "", "educators, leaders and anyone who presents", "What live television teaches about clarity, presence and staying calm when the teleprompter fails.")}
      </ul>
    </div>

    <div class="offer reveal">
      <div class="offer-side">
        <h2>Training Workshops</h2>
        <p>Interactive, hands-on sessions where participants apply ideas to their own courses and leave with a plan.</p>
        <p class="price">Virtual or in person &middot; connect for pricing</p>
        <a class="btn" href="contact.html">Host a workshop</a>
      </div>
      <ul class="offer-list">
        {offer_item("AI-Ready Assignments", "90&ndash;120 minutes", "faculty and instructional designers", "Redesign one real assignment so it supports learning in a world where students have AI &mdash; with clear expectations and authentic assessment.")}
        {offer_item("Writing Your Course AI Policy", "60&ndash;90 minutes", "faculty and department chairs", "Draft a clear, fair syllabus statement on AI use, informed by your discipline and learning outcomes.")}
        {offer_item("Online Course Makeover", "90&ndash;120 minutes", "online and hybrid instructors", "Apply quality design principles to an existing course: navigation, alignment, accessibility and engagement.")}
        {offer_item("Teaching on Camera", "60&ndash;90 minutes", "instructors recording video", "Broadcast techniques for recorded lectures and live sessions &mdash; scripting, delivery and simple production that looks professional.")}
        {offer_item("Active Learning, Any Modality", "60&ndash;90 minutes", "all instructors", "Practical strategies for discussion, collaboration and retrieval practice in person and online.")}
      </ul>
    </div>

    <div class="offer reveal">
      <div class="offer-side">
        <h2>Full-Day Institute</h2>
        <p>A deeper, customized experience for teams ready to make lasting change.</p>
        <p class="price">Virtual or on-site &middot; connect for pricing</p>
        <a class="btn" href="contact.html">Host an institute</a>
      </div>
      <ul class="offer-list">
        {offer_item("From Reactive to Intentional: Teaching and Technology", "full day", "departments, teaching centers and faculty cohorts", "Combines strategy, hands-on design time and tailored application, so participants leave with redesigned course materials and a shared approach to AI.")}
      </ul>
    </div>

    <div class="offer reveal">
      <div class="offer-side">
        <h2>Author Events</h2>
        <p>For libraries, book festivals and book clubs, in person or online.</p>
        <a class="btn" href="contact.html">Invite Laura</a>
      </div>
      <ul class="offer-list">
        {offer_item("Secrets, Lies &amp; Southern Settings", "45&ndash;60 minutes", "readers, libraries and book festivals", "Writing suspense, the road from newsroom to novelist, and writing under two names &mdash; with Q&amp;A and signing.")}
      </ul>
    </div>
  </div>
</section>

<section class="cta-band on-dark" id="book" style="scroll-margin-top:72px">
  <div class="wrap reveal">
    <h3 style="font-size:clamp(1.6rem,3vw,2.2rem)">Not quite ready to schedule a session? Start with the free guide, <em>10 Questions to Ask Before Bringing AI Into Your Course</em>.</h3>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="ai-questions.html">Read the guide</a>
      <a class="btn ghost" href="contact.html">Check availability</a>
    </div>
  </div>
</section>
"""

SHORT_BIO = "Dr. Laura McNeill is a professor of instructional technology at The University of Alabama, a former award-winning TV news anchor, and the author of the suspense novels <em>Center of Gravity</em>, <em>Sister Dear</em> and <em>The World Breaks Everyone</em>. She also writes women&rsquo;s fiction as Lauren Clark."
LONG_BIO = "Dr. Laura McNeill is a professor of instructional technology at The University of Alabama, where she also serves as an instructional consultant for the university&rsquo;s Teaching Academy. She holds a Ph.D. in Instructional Leadership with a concentration in Instructional Technology from The University of Alabama, along with an M.S. in Interactive Technology and an M.A. in Journalism and Public Relations.</p><p>Before entering higher education, Laura spent six years behind the anchor desk at two CBS affiliates, earning awards from the Associated Press. She is the author of three suspense novels &mdash; <em>Center of Gravity</em> (2015) and <em>Sister Dear</em> (2016), published by Thomas Nelson, an imprint of HarperCollins, and <em>The World Breaks Everyone</em> (2018) &mdash; and writes award-winning women&rsquo;s fiction under the name Lauren Clark.</p><p>Laura speaks and consults on teaching in the age of AI, engaging course design, educational technology and communication. She lives in Alabama."
INTRO = "Our next speaker has spent her career telling stories &mdash; first as an award-winning television news anchor, then as a novelist, and now as a professor of instructional technology at The University of Alabama. She is the author of three suspense novels and helps educators use technology with purpose. Please welcome Dr. Laura McNeill."

def bio_block(id_, label, words, html):
    return f"""<div class="bio-block reveal">
  <div class="bio-head"><h3>{label}</h3><span class="meta">{words}</span><button class="copy-btn" type="button" data-copy="{id_}">Copy</button></div>
  <div class="bio-text" id="{id_}"><p>{html}</p></div>
</div>"""

media = f"""
<section class="pro-hero on-dark solo">
  <div class="wrap reveal">
    <h1>Media</h1>
    <p class="lede">From the anchor desk to the bookstore to the classroom, Laura brings clarity, warmth and a storyteller&rsquo;s voice to conversations about teaching, technology and writing.</p>
    <div class="btn-row"><a class="btn" href="#kit">Get the media kit</a><a class="btn ghost" href="#press-contact">Press inquiries</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <h2 class="reveal" style="text-align:center;margin-bottom:40px">Milestones &amp; press</h2>
    <ul class="press reveal">
      <li><span class="when">2018</span><h3><em>The World Breaks Everyone</em> published</h3><p>Laura&rsquo;s third suspense novel follows sixteen-year-old Olivia on the run from danger.</p></li>
      <li><span class="when">2016</span><h3><em>Sister Dear</em> published by Thomas Nelson</h3><p>A mother paroled after ten years returns home to the daughter she left behind. Reviewed by <em>Publishers Weekly</em>.</p></li>
      <li><span class="when">2015</span><h3>Debut novel <em>Center of Gravity</em></h3><p>Published by Thomas Nelson, an imprint of HarperCollins, and set on the Alabama Gulf Coast.</p></li>
    </ul>
  </div>
</section>

<section class="section-alt" id="kit" style="scroll-margin-top:72px">
  <div class="wrap split">
    <div class="reveal">{BLOB}<p style="text-align:center;color:var(--muted);font-size:.9rem;margin-top:14px">High-resolution headshot available on request</p></div>
    <div>
      <h2 class="reveal">Media kit</h2>
      {bio_block("bio-short", "Short bio", "~50 words", SHORT_BIO)}
      {bio_block("bio-long", "Full bio", "~150 words", LONG_BIO)}
    </div>
  </div>
</section>

<section id="facts" style="scroll-margin-top:72px">
  <div class="wrap">
    <h2 class="reveal" style="margin-bottom:32px">Fast facts</h2>
    <dl class="facts-grid reveal">
      <div><dt>Role</dt><dd>Professor of Instructional Technology, The University of Alabama</dd></div>
      <div><dt>Education</dt><dd>Ph.D., Instructional Leadership (Instructional Technology) &middot; M.S., Interactive Technology &middot; M.A., Journalism &amp; PR</dd></div>
      <div><dt>Broadcast</dt><dd>Six years as a news anchor at two CBS affiliates; Associated Press awards</dd></div>
      <div><dt>Novels</dt><dd><em>Center of Gravity</em> (2015) &middot; <em>Sister Dear</em> (2016) &middot; <em>The World Breaks Everyone</em> (2018)</dd></div>
      <div><dt>Publisher</dt><dd>Thomas Nelson, an imprint of HarperCollins</dd></div>
      <div><dt>Pen name</dt><dd>Lauren Clark &mdash; women&rsquo;s fiction</dd></div>
    </dl>
  </div>
</section>

<section class="section-alt" id="topics" style="scroll-margin-top:72px">
  <div class="wrap split">
    <div class="reveal">
      <h2>Interview topics</h2>
      <p style="color:var(--paper-dim)">Laura is an experienced interviewee &mdash; and a former interviewer.</p>
    </div>
    <ul class="audience reveal">
      <li><strong>AI in the classroom</strong><span>What generative AI means for teaching, assessment and academic integrity.</span></li>
      <li><strong>Online &amp; hybrid learning</strong><span>What makes a course engaging, and why so many aren&rsquo;t.</span></li>
      <li><strong>Newsroom to classroom</strong><span>A career in broadcast news and what it taught her about teaching.</span></li>
      <li><strong>Writing suspense</strong><span>Family secrets, Southern settings and building a twist that lands.</span></li>
      <li><strong>Two names, two genres</strong><span>Suspense as Laura McNeill; women&rsquo;s fiction as Lauren Clark.</span></li>
    </ul>
  </div>
</section>

<section id="intro" style="scroll-margin-top:72px">
  <div class="wrap" style="max-width:860px">
    {bio_block("speaker-intro", "Speaker introduction", "~30 seconds read aloud", INTRO)}
  </div>
</section>

<section class="cta-band on-dark" id="press-contact" style="scroll-margin-top:72px">
  <div class="wrap reveal">
    <h2>Interview requests &amp; review copies</h2>
    <p>For interviews, podcasts, high-resolution headshots and book cover images, please get in touch.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="contact.html">Contact Laura</a>
      <a class="btn ghost" href="speaking.html">Speaking topics</a>
    </div>
  </div>
</section>
"""

def q(title, text, ask):
    return f'<li><div><h3>{title}</h3><p>{text}</p><p class="ask">Ask yourself: {ask}</p></div></li>'

guide = f"""
<section class="pro-hero on-dark solo">
  <div class="wrap reveal">
    <p class="eyebrow">Free guide</p>
    <h1>10 Questions to Ask Before Bringing AI Into Your Course</h1>
    <p class="lede">A practical checklist for faculty, instructional designers and academic leaders. Work through it before you redesign, restrict or embrace AI &mdash; and you&rsquo;ll make decisions you can explain to students and stand behind.</p>
    <div class="btn-row"><button class="btn" type="button" onclick="window.print()">Print or save as PDF</button><a class="btn ghost" href="consulting.html#services">Get support</a></div>
  </div>
</section>

<section>
  <div class="wrap">
    <ol class="qs">
      {q("What should students be able to do without AI?", "Start with your learning outcomes, not the tools. Some skills must be practiced unaided to be learned at all; others can be extended or accelerated with help.", "Which outcomes would be hollowed out if AI did the work?")}
      {q("Where could AI genuinely support learning?", "AI can give feedback on drafts, generate practice questions, explain concepts another way or model expert thinking. Look for places where it adds practice, not shortcuts.", "Where do my students get stuck, and could AI help them get unstuck without doing the thinking for them?")}
      {q("What is my policy &mdash; and can I explain why?", "Students follow policies they understand. A clear rationale, tied to your discipline and outcomes, matters more than whether the answer is &ldquo;yes,&rdquo; &ldquo;no&rdquo; or &ldquo;it depends.&rdquo;", "Could a student explain my AI policy, and the reason for it, in two sentences?")}
      {q("Does the policy change by assignment?", "One rule rarely fits a whole course. Labeling each assignment &mdash; AI not allowed, allowed with disclosure, or encouraged &mdash; removes guesswork.", "Have I marked AI expectations on every major assignment?")}
      {q("Which assessments are most vulnerable?", "Generic prompts with a single polished product are easiest to outsource. Process work, personal connection, local context and in-class components are more resilient.", "Which assignments could be completed convincingly by AI in five minutes?")}
      {q("How will students show their thinking?", "Drafts, reflections, annotated sources, oral check-ins and revision histories make learning visible &mdash; and make the final product only part of the story.", "Where in this assignment does a student&rsquo;s reasoning become visible to me?")}
      {q("Is access equitable?", "Not every student has the same devices, paid tools or prior experience. If AI use is expected, make sure everyone has a fair, supported way in.", "If I require or allow AI, can every student access a suitable tool at no cost?")}
      {q("What about privacy and data?", "Student work and personal information shouldn&rsquo;t be fed into tools without understanding where it goes. Check your institution&rsquo;s approved tools and data guidance.", "Do I know what happens to anything my students (or I) put into this tool?")}
      {q("How will I teach students to use AI well?", "Students need guidance on prompting, checking accuracy, citing use and recognizing bias &mdash; skills that don&rsquo;t develop on their own.", "Where in the course do I model and practice responsible AI use?")}
      {q("How will I know if it&rsquo;s working?", "Treat AI changes like any course redesign: gather evidence. Compare outcomes, ask students what helped, and adjust next term.", "What will I look at at the end of the term to decide whether to keep, change or drop this approach?")}
    </ol>
  </div>
</section>

<section class="cta-band on-dark">
  <div class="wrap reveal">
    <h2>Want help putting these into practice?</h2>
    <p>Laura leads workshops on AI-ready assignments and course AI policies, and consults with departments and teaching centers.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="contact.html">Book a call</a>
      <a class="btn ghost" href="speaking.html">View workshops</a>
    </div>
  </div>
</section>
"""

pages = {
 "index.html": ("Laura McNeill — Author of Suspense", "Official site of suspense novelist Laura McNeill, author of Center of Gravity, Sister Dear and The World Breaks Everyone.", home),
 "books.html": ("Books — Laura McNeill", "Novels by Laura McNeill, plus women's fiction written as Lauren Clark.", books),
 "about.html": ("About — Laura McNeill", "Laura McNeill: suspense novelist, former award-winning TV news anchor, and professor of instructional technology.", about),
 "consulting.html": ("Consulting — Dr. Laura McNeill", "Instructional design, faculty development, AI and educational technology consulting, and speaking from Dr. Laura McNeill.", consulting),
 "speaking.html": ("Training & Speaking — Dr. Laura McNeill", "Keynotes, training workshops, full-day institutes and author events from Dr. Laura McNeill.", speaking),
 "ai-questions.html": ("10 Questions to Ask Before Bringing AI Into Your Course — Dr. Laura McNeill", "A free guide for faculty and instructional leaders: ten questions to work through before bringing AI into a course.", guide),
 "media.html": ("Media Kit — Laura McNeill", "Media and press kit for Dr. Laura McNeill: approved bios, fast facts, interview topics and speaker introduction.", media),
 "contact.html": ("Contact — Laura McNeill", "Book club, media, speaking and academic inquiries for author Laura McNeill.", contact),
}
for fn, (t, d, b) in pages.items():
    with open(os.path.join(OUT, fn), "w") as fh:
        fh.write(page(fn, t, d, b))
print("ok")
