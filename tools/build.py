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

NAV = [("index.html", "Home"), ("books.html", "Books"), ("about.html", "About"), ("consulting.html", "Consulting"), ("speaking.html", "Speaking"), ("media.html", "Media"), ("contact.html", "Contact")]

def page(fname, title, desc, body):
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
<meta name="theme-color" content="#0d0f14">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="wordmark" href="index.html">Laura <span>McNeill</span></a>
    <button class="menu-btn" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <nav class="nav" id="site-nav" aria-label="Main">
{nav}
    </nav>
  </div>
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


# ---------------- CONSULTING ----------------
def svc(n, title, text, items):
    li = "".join(f"<li>{i}</li>" for i in items)
    return f'<article class="service reveal"><div class="num">{n}</div><h3>{title}</h3><p>{text}</p><ul>{li}</ul></article>'

consulting = f"""
<header class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Consulting &amp; Speaking</p>
    <h1>Teaching that <em style="color:var(--brass-bright)">works</em>,<br>technology that serves it.</h1>
    <p>Dr. Laura McNeill helps universities, schools and organizations design courses people actually finish, bring technology and AI into teaching with purpose, and tell their story clearly &mdash; drawing on a Ph.D. in instructional technology, years of faculty development, and a career in broadcast news.</p>
    <div class="btn-row">
      <a class="btn" href="#start">Start a conversation</a>
      <a class="btn ghost" href="#services">View services</a>
    </div>
  </div>
</header>

<section id="services" style="scroll-margin-top:72px">
  <div class="wrap">
    <div class="section-head reveal">
      <div><p class="eyebrow">Services</p><h2>How I can help</h2></div>
    </div>
    <div class="services">
      {svc("01", "Course &amp; Program Design", "Evidence-based design for online, hybrid and face-to-face courses &mdash; from a single module to a full program.", ["Online and hybrid course builds", "Learning outcomes &amp; alignment", "Quality reviews of existing courses", "Accessible, engaging materials"])}
      {svc("02", "Faculty Development", "Workshops and consultations that help instructors teach with confidence, drawn from work with The University of Alabama&rsquo;s Teaching Academy.", ["Interactive workshops &amp; institutes", "One-on-one teaching consultations", "Active learning strategies", "Teaching with video &amp; media"])}
      {svc("03", "AI &amp; Educational Technology", "Practical, research-informed guidance on choosing and using technology &mdash; including generative AI &mdash; in ways that support learning.", ["AI policies &amp; classroom guidelines", "Tool selection &amp; rollout planning", "Assignment redesign for the AI era", "Technology integration coaching"])}
      {svc("04", "Media &amp; Communication", "Six years as an award-winning TV anchor, put to work for educators and leaders who need to communicate on camera and on the page.", ["On-camera &amp; presentation coaching", "Instructional video production", "Writing for clarity &amp; impact", "Storytelling for programs &amp; research"])}
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Who I work with</p>
      <h2>Partners in learning</h2>
      <p style="color:var(--paper-dim)">Engagements are shaped around your people, your timeline and your goals &mdash; whether that&rsquo;s a single keynote or a semester-long redesign.</p>
    </div>
    <ul class="audience reveal">
      <li><strong>Colleges &amp; universities</strong><span>Centers for teaching, online learning offices, departments and faculty cohorts.</span></li>
      <li><strong>K&ndash;12 schools &amp; districts</strong><span>Technology integration and professional learning for teachers and leaders.</span></li>
      <li><strong>Organizations &amp; nonprofits</strong><span>Training design, onboarding programs and learning content for adult learners.</span></li>
      <li><strong>Writers &amp; communicators</strong><span>Talks and workshops on storytelling, publishing and writing across genres.</span></li>
    </ul>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Process</p><h2>How an engagement works</h2></div></div>
    <ol class="steps reveal">
      <li><span class="step-n">1</span><h3>Listen</h3><p>A free introductory call to understand your learners, your challenges and what success looks like.</p></li>
      <li><span class="step-n">2</span><h3>Plan</h3><p>A clear proposal with scope, deliverables and timeline &mdash; no surprises.</p></li>
      <li><span class="step-n">3</span><h3>Build</h3><p>Collaborative design and delivery, with regular check-ins and room for feedback.</p></li>
      <li><span class="step-n">4</span><h3>Sustain</h3><p>Resources, guides and follow-up so the work keeps going after the engagement ends.</p></li>
    </ol>
  </div>
</section>

<section class="section-alt">
  <div class="wrap split reverse">
    <div class="reveal">
      <div class="portrait"><span class="mono">L<i>M</i></span><span class="cap">Dr. Laura McNeill</span></div>
    </div>
    <div class="reveal">
      <p class="eyebrow">Background</p>
      <h2>Researcher, teacher, storyteller.</h2>
      <ul class="creds">
        <li><strong>Ph.D.</strong> Instructional Leadership, Instructional Technology concentration &mdash; The University of Alabama</li>
        <li><strong>M.S.</strong> Interactive Technology</li>
        <li><strong>M.A.</strong> Journalism &amp; Public Relations</li>
        <li><strong>Professor</strong> of Instructional Technology, The University of Alabama</li>
        <li><strong>Instructional consultant</strong>, UA Teaching Academy</li>
        <li><strong>Award-winning anchor</strong> &mdash; six years at two CBS affiliates, honored by the Associated Press</li>
        <li><strong>Novelist</strong> &mdash; published by Thomas Nelson / HarperCollins</li>
      </ul>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Speaking</p><h2>Keynotes &amp; workshops</h2></div><a class="more" href="speaking.html">All talks &amp; booking &rarr;</a></div>
    <div class="pillars reveal">
      <div class="pillar"><div class="num">I.</div><h3>Teaching in the age of AI</h3><p>What generative AI changes about learning, assessment and academic integrity &mdash; and what it doesn&rsquo;t.</p></div>
      <div class="pillar"><div class="num">II.</div><h3>Designing for engagement</h3><p>Practical strategies for courses that hold attention online, in person, and everywhere in between.</p></div>
      <div class="pillar"><div class="num">III.</div><h3>The story behind the story</h3><p>Lessons from the newsroom and the novel on communicating clearly and memorably.</p></div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">FAQ</p>
      <h2>Good questions</h2>
    </div>
    <div class="faq reveal">
      <details><summary>Do you work remotely?</summary><p>Yes. Most consulting and many workshops happen virtually; on-site visits can be arranged for keynotes, institutes and multi-day engagements.</p></details>
      <details><summary>How are engagements priced?</summary><p>Every project is scoped individually. After an introductory call you&rsquo;ll receive a proposal with a fixed fee or a clear hourly estimate.</p></details>
      <details><summary>Can you work with our existing LMS and tools?</summary><p>Yes. Recommendations start from the platforms and resources you already have, and only add new tools when they clearly serve your learners.</p></details>
      <details><summary>How far ahead should we book?</summary><p>For keynotes and workshops, four to eight weeks is ideal. Course design projects depend on scope &mdash; reach out early so the timeline fits your term.</p></details>
    </div>
  </div>
</section>

<section class="cta-band" id="start" style="scroll-margin-top:72px">
  <div class="wrap reveal">
    <p class="eyebrow">Let&rsquo;s talk</p>
    <h2>Have a project in mind?</h2>
    <p>Tell me about your learners, your goals and your timeline. I&rsquo;ll follow up to schedule a free introductory call.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="contact.html">Get in touch</a>
      <a class="btn ghost" href="https://sites.ua.edu/lmcneill" target="_blank" rel="noopener">Faculty profile</a>
    </div>
  </div>
</section>
"""

# ---------------- SPEAKING ----------------
def talk(n, kind, title, text, takeaways):
    t = "".join(f"<li>{x}</li>" for x in takeaways)
    return f"""<article class="talk reveal">
  <div class="talk-n">{n}</div>
  <div>
    <p class="talk-kind">{kind}</p>
    <h3>{title}</h3>
    <p>{text}</p>
    <ul>{t}</ul>
  </div>
</article>"""

speaking = f"""
<header class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Speaking</p>
    <h1>A broadcaster&rsquo;s presence.<br>An educator&rsquo;s <em style="color:var(--brass-bright)">substance</em>.</h1>
    <p>Dr. Laura McNeill brings six years of live television, a Ph.D. in instructional technology and a novelist&rsquo;s sense of story to every stage &mdash; leaving audiences with ideas they can use on Monday morning.</p>
    <div class="btn-row">
      <a class="btn" href="#book">Book Laura</a>
      <a class="btn ghost" href="media.html">Speaker kit &amp; bios</a>
    </div>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Signature Talks</p><h2>Topics</h2></div></div>
    <div class="talks">
      {talk("01", "Keynote &middot; Workshop", "Teaching in the Age of AI", "Generative AI has changed what students can do in a single prompt. This session cuts through the noise to look at what actually changes about learning, assessment and integrity &mdash; and what stays the same.", ["A clear-eyed framework for when AI helps learning and when it gets in the way", "Assignment redesign strategies faculty can apply immediately", "Starting points for course and campus AI guidelines"])}
      {talk("02", "Keynote &middot; Workshop", "Designing for Engagement", "Whether a course is online, hybrid or face-to-face, attention is earned. Drawing on instructional design research and years of faculty development, Laura shares practical ways to build courses learners want to finish.", ["Evidence-based design moves for any modality", "Using video, media and interaction with purpose", "Quick wins for existing courses"])}
      {talk("03", "Keynote &middot; Training", "From the Anchor Desk: Communicating with Confidence", "What live television teaches about clarity, presence and staying calm when the teleprompter fails. Built for educators, leaders and anyone who presents, records or teaches on camera.", ["On-camera and presentation techniques from broadcast news", "Structuring a message people remember", "Practical tips for recorded lectures and video"])}
      {talk("04", "Author Talk", "Secrets, Lies &amp; Southern Settings", "For libraries, book festivals and reader events: Laura talks about writing suspense, the journey from newsroom to novelist, and why every family has a story it would rather not tell.", ["Behind the scenes of <em>Center of Gravity</em>, <em>Sister Dear</em> and <em>The World Breaks Everyone</em>", "Writing under two names in two genres", "Q&amp;A and signing"])}
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">Formats</p><h2>Built for your event</h2></div></div>
    <div class="formats reveal">
      <div><h3>Keynote</h3><p>45&ndash;60 minutes. An energizing opener or closer for conferences, convocations and kickoffs.</p></div>
      <div><h3>Workshop</h3><p>90 minutes to a full day. Hands-on, interactive sessions with take-home resources.</p></div>
      <div><h3>Panel &amp; moderation</h3><p>A former anchor who keeps the conversation moving and the questions sharp.</p></div>
      <div><h3>Virtual</h3><p>Live, engaging online sessions &mdash; designed for the screen, not adapted to it.</p></div>
      <div><h3>Author events</h3><p>Library talks, book festivals and book club visits, in person or online.</p></div>
    </div>
  </div>
</section>

<section>
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Audiences</p>
      <h2>Who invites Laura</h2>
      <p style="color:var(--paper-dim)">Talks are tailored to each audience, with examples and activities that fit their work.</p>
    </div>
    <ul class="audience reveal">
      <li><strong>Higher education</strong><span>Teaching centers, faculty institutes, online learning and academic leadership.</span></li>
      <li><strong>K&ndash;12 educators</strong><span>Professional learning days, technology integration and instructional coaching.</span></li>
      <li><strong>Professional associations</strong><span>Conferences on education, technology, communication and media.</span></li>
      <li><strong>Libraries &amp; book festivals</strong><span>Author talks, writing workshops and reader events.</span></li>
    </ul>
  </div>
</section>

<section class="cta-band section-alt" id="book" style="scroll-margin-top:72px">
  <div class="wrap reveal">
    <p class="eyebrow">Booking</p>
    <h2>Bring Laura to your event</h2>
    <p>Share your date, location, audience and format, and Laura will follow up about availability. Event organizers will find bios, fast facts and a speaker introduction in the media kit.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="contact.html">Request availability</a>
      <a class="btn ghost" href="media.html">Media &amp; speaker kit</a>
    </div>
  </div>
</section>
"""

# ---------------- MEDIA ----------------
SHORT_BIO = "Dr. Laura McNeill is a professor of instructional technology at The University of Alabama, a former award-winning TV news anchor, and the author of the suspense novels <em>Center of Gravity</em>, <em>Sister Dear</em> and <em>The World Breaks Everyone</em>. She also writes women&rsquo;s fiction as Lauren Clark."
LONG_BIO = "Dr. Laura McNeill is a professor of instructional technology at The University of Alabama, where she also serves as an instructional consultant for the university&rsquo;s Teaching Academy. She holds a Ph.D. in Instructional Leadership with a concentration in Instructional Technology from The University of Alabama, along with an M.S. in Interactive Technology and an M.A. in Journalism and Public Relations.</p><p>Before entering higher education, Laura spent six years behind the anchor desk at two CBS affiliates, earning awards from the Associated Press. She is the author of three suspense novels &mdash; <em>Center of Gravity</em> (2015) and <em>Sister Dear</em> (2016), published by Thomas Nelson, an imprint of HarperCollins, and <em>The World Breaks Everyone</em> (2018) &mdash; and writes award-winning women&rsquo;s fiction under the name Lauren Clark.</p><p>Laura speaks and consults on teaching in the age of AI, engaging course design, educational technology and communication. She lives in Alabama."
INTRO = "Our next speaker has spent her career telling stories &mdash; first as an award-winning television news anchor, then as a novelist, and now as a professor of instructional technology at The University of Alabama. She is the author of three suspense novels and helps educators use technology with purpose. Please welcome Dr. Laura McNeill."

def bio_block(id_, label, words, html):
    return f"""<div class="bio-block reveal">
  <div class="bio-head"><h3>{label}</h3><span class="meta">{words}</span><button class="copy-btn" type="button" data-copy="{id_}">Copy</button></div>
  <div class="bio-text" id="{id_}"><p>{html}</p></div>
</div>"""

media = f"""
<header class="page-hero">
  <div class="wrap">
    <p class="eyebrow">Media &amp; Press</p>
    <h1>Media kit</h1>
    <p>Everything journalists, podcast hosts and event organizers need: approved bios, fast facts, interview topics and a ready-to-read introduction.</p>
    <nav class="tabs" aria-label="Jump to section">
      <a href="#bios">Bios</a><a href="#facts">Fast facts</a><a href="#topics">Interview topics</a><a href="#intro">Speaker intro</a><a href="#press-contact">Contact</a>
    </nav>
  </div>
</header>

<section id="bios" style="scroll-margin-top:72px">
  <div class="wrap split">
    <div class="reveal">
      <div class="portrait"><span class="mono">L<i>M</i></span><span class="cap">Headshot available on request</span></div>
    </div>
    <div>
      <p class="eyebrow reveal">Approved Bios</p>
      {bio_block("bio-short", "Short bio", "~50 words", SHORT_BIO)}
      {bio_block("bio-long", "Full bio", "~150 words", LONG_BIO)}
    </div>
  </div>
</section>

<section class="section-alt" id="facts" style="scroll-margin-top:72px">
  <div class="wrap">
    <div class="section-head reveal"><div><p class="eyebrow">At a glance</p><h2>Fast facts</h2></div></div>
    <dl class="facts-grid reveal">
      <div><dt>Role</dt><dd>Professor of Instructional Technology, The University of Alabama</dd></div>
      <div><dt>Education</dt><dd>Ph.D., Instructional Leadership (Instructional Technology) &middot; M.S., Interactive Technology &middot; M.A., Journalism &amp; PR</dd></div>
      <div><dt>Broadcast</dt><dd>Six years as a news anchor at two CBS affiliates; Associated Press awards</dd></div>
      <div><dt>Novels</dt><dd><em>Center of Gravity</em> (2015) &middot; <em>Sister Dear</em> (2016) &middot; <em>The World Breaks Everyone</em> (2018)</dd></div>
      <div><dt>Publisher</dt><dd>Thomas Nelson, an imprint of HarperCollins</dd></div>
      <div><dt>Pen name</dt><dd>Lauren Clark &mdash; women&rsquo;s fiction</dd></div>
      <div><dt>Based in</dt><dd>Alabama</dd></div>
    </dl>
  </div>
</section>

<section id="topics" style="scroll-margin-top:72px">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">For interviews &amp; podcasts</p>
      <h2>Conversation starters</h2>
      <p style="color:var(--paper-dim)">Laura is an experienced interviewee &mdash; and a former interviewer. Topics she&rsquo;s glad to discuss:</p>
    </div>
    <ul class="audience reveal">
      <li><strong>AI in the classroom</strong><span>What generative AI means for teaching, assessment and academic integrity.</span></li>
      <li><strong>Online &amp; hybrid learning</strong><span>What makes a course engaging, and why so many aren&rsquo;t.</span></li>
      <li><strong>Newsroom to classroom</strong><span>A career in broadcast news and what it taught her about teaching.</span></li>
      <li><strong>Writing suspense</strong><span>Family secrets, Southern settings and building a twist that lands.</span></li>
      <li><strong>Two names, two genres</strong><span>Writing suspense as Laura McNeill and women&rsquo;s fiction as Lauren Clark.</span></li>
    </ul>
  </div>
</section>

<section class="section-alt" id="intro" style="scroll-margin-top:72px">
  <div class="wrap" style="max-width:860px">
    <p class="eyebrow reveal">For event hosts</p>
    {bio_block("speaker-intro", "Speaker introduction", "~30 seconds read aloud", INTRO)}
  </div>
</section>

<section class="cta-band" id="press-contact" style="scroll-margin-top:72px">
  <div class="wrap reveal">
    <p class="eyebrow">Press inquiries</p>
    <h2>Interview requests &amp; review copies</h2>
    <p>For interviews, podcast appearances, high-resolution headshots and book cover images, please get in touch.</p>
    <div class="btn-row" style="justify-content:center">
      <a class="btn" href="contact.html">Contact Laura</a>
      <a class="btn ghost" href="speaking.html">Speaking topics</a>
    </div>
  </div>
</section>
"""

pages = {
 "index.html": ("Laura McNeill — Author of Suspense", "Official site of suspense novelist Laura McNeill, author of Center of Gravity, Sister Dear and The World Breaks Everyone.", home),
 "books.html": ("Books — Laura McNeill", "Novels by Laura McNeill, plus women's fiction written as Lauren Clark.", books),
 "about.html": ("About — Laura McNeill", "Laura McNeill: suspense novelist, former award-winning TV news anchor, and professor of instructional technology.", about),
 "consulting.html": ("Consulting — Dr. Laura McNeill", "Instructional design, faculty development, AI and educational technology consulting, and speaking from Dr. Laura McNeill.", consulting),
 "speaking.html": ("Speaking — Dr. Laura McNeill", "Keynotes, workshops and author talks from Dr. Laura McNeill on AI in teaching, course design, communication and writing suspense.", speaking),
 "media.html": ("Media Kit — Laura McNeill", "Media and press kit for Dr. Laura McNeill: approved bios, fast facts, interview topics and speaker introduction.", media),
 "contact.html": ("Contact — Laura McNeill", "Book club, media, speaking and academic inquiries for author Laura McNeill.", contact),
}
for fn, (t, d, b) in pages.items():
    with open(os.path.join(OUT, fn), "w") as fh:
        fh.write(page(fn, t, d, b))
print("ok")
