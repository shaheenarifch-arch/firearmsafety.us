import os,json,datetime
import pathlib; OUT=str(pathlib.Path(__file__).resolve().parent.parent)
DOM='https://firearmsafety.us'
UDT='https://www.awin1.com/cread.php?awinmid=128023&amp;awinaffid=3067297'
TODAY='2026-10-20'
BANNERS=['4893624','4893620','4893619','4893622']
def banner(i):
    b=BANNERS[i%len(BANNERS)]
    return f'<a class="bnr" rel="sponsored nofollow noopener" target="_blank" href="https://www.awin1.com/cread.php?s={b}&amp;v=128023&amp;q=615217&amp;r=3067297"><img src="https://www.awin1.com/cshow.php?s={b}&amp;v=128023&amp;q=615217&amp;r=3067297" alt="United Defense Tactical firearm training classes" loading="lazy" decoding="async"></a>'
def IMG(pid,w=1200,h=None):
    return f'https://images.unsplash.com/photo-{pid}?auto=format&amp;fit=crop&amp;w={w}{"&amp;h="+str(h) if h else ""}&amp;q=70'
PH={'fronds':'1621146027714-e8921770f8d0','canopy':'1699575678956-aefa714b67f0','instructor':'1788077510419-66aed12de0b7',
'woman':'1761144530756-47ecd564f8ef','target':'1577905027671-c5cc33c825ed','leaves':'1584069453523-76e1b64154c4',
'path':'1632037667990-227e49f350c6','bridge':'1768357774088-cee45602e2bb','coach':'1788077084639-c104e8d16228','indoor':'1577905027675-fcbe1521b1c8'}
# Original woodland camo tile (inline SVG, no external assets)
CAMO=("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240' viewBox='0 0 240 240'%3E"
"%3Crect width='240' height='240' fill='%23243320'/%3E"
"%3Cpath fill='%23384a2a' d='M0 30c30-22 62-8 80 10s40 14 58-4 50-10 52 18-30 40-60 34-40 20-70 12S-6 70 0 30zM150 150c20-16 52-10 70 6s28 44 4 56-44-4-66 2-46-6-40-28 12-20 32-36z'/%3E"
"%3Cpath fill='%235a5a32' d='M20 140c18-14 46-6 52 12s-6 34-28 36-40-10-40-24 2-12 16-24zM120 60c14-10 36-8 44 6s-4 30-22 30-36-4-36-16 2-10 14-20zM190 90c12-6 30 2 32 16s-12 22-26 18-18-28-6-34z'/%3E"
"%3Cpath fill='%2314190f' d='M60 90c10-8 26-4 30 6s-4 20-18 20-22-6-22-12 2-8 10-14zM170 30c8-6 20-2 22 6s-4 14-14 14-16-4-14-10 0-6 6-10zM90 200c10-6 24-2 26 8s-6 18-18 16-18-8-16-14 2-6 8-10zM210 180c8-4 18 0 18 8s-8 12-16 10-10-14-2-18z'/%3E"
"%3Cpath fill='%237d7448' d='M100 120c8-4 18 0 18 8s-8 12-16 10-10-14-2-18zM30 210c6-4 14 0 14 6s-6 10-12 8-8-10-2-14zM220 50c6-4 14 0 14 6s-6 10-12 8-8-10-2-14z'/%3E"
"%3C/svg%3E")
CSS=r"""
:root{color-scheme:dark;--night:#0C130E;--bg:#101912;--panel:#15211A;--panel2:#1B2A20;--moss:#2E4A2B;--olive:#6E7B3B;--khaki:#C8B98B;--ink:#E9EBDD;--muted:#A3AE94;--line:#2B3B2D;--blaze:#F07A1E;--blaze-ink:#FF9A4A;--signal:#D9C46A}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%;scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:400 1.1rem/1.7 "Barlow",system-ui,sans-serif;overflow-x:hidden}
img{max-width:100%}
a{color:inherit;text-decoration-color:var(--blaze);text-underline-offset:3px;text-decoration-thickness:2px}
a:hover{color:var(--blaze-ink)}
:focus-visible{outline:3px solid var(--blaze);outline-offset:3px}
h1,h2,h3,.brand,.nav a,.btn,.guides b,.post-card b,.rules b{font-family:"Barlow Condensed","Barlow",sans-serif;text-transform:uppercase;letter-spacing:.02em}
h1{font-family:"Saira Stencil One","Barlow Condensed",sans-serif;font-weight:400;font-size:clamp(2.3rem,6.4vw,4.2rem);line-height:1.02;letter-spacing:.01em;margin:0 0 .45em;text-transform:uppercase}
h2{font-weight:700;font-size:clamp(1.55rem,3.4vw,2.1rem);line-height:1.1;margin:2.1em 0 .5em}
h3{font-weight:700;font-size:1.25rem;margin:1.6em 0 .3em}
p,li{max-width:70ch}
.mono,.kicker,.hud,.rule-n,.meta{font-family:"Share Tech Mono",ui-monospace,monospace;letter-spacing:.08em}
.kicker{display:inline-flex;align-items:center;gap:10px;font-size:.82rem;color:var(--signal);text-transform:uppercase;margin-bottom:14px}
.kicker:before{content:"";width:28px;height:2px;background:var(--blaze)}
.wrap{max-width:1140px;margin:0 auto;padding:0 20px}
.skip{position:absolute;left:-999px}.skip:focus{left:12px;top:12px;background:var(--blaze);color:#000;padding:8px 12px;z-index:10}
header.top{position:sticky;top:0;z-index:5;background:rgba(12,19,14,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line)}
header.top:before{content:"";display:block;height:6px;background:url("CAMO") 0 0/240px}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:14px;padding-top:12px;padding-bottom:12px;flex-wrap:wrap}
.brand{font-weight:700;font-size:1.35rem;text-decoration:none;display:flex;align-items:center;gap:10px;letter-spacing:.06em}
.brand i{display:inline-grid;place-items:center;width:30px;height:30px;border:2px solid var(--blaze);border-radius:50%;position:relative}
.brand i:before,.brand i:after{content:"";position:absolute;background:var(--blaze)}
.brand i:before{width:2px;height:36px}.brand i:after{width:36px;height:2px}
.brand em{font-style:normal;color:var(--blaze)}
.nav{display:flex;gap:4px 18px;flex-wrap:wrap}
.nav a{font-size:1rem;font-weight:600;text-decoration:none;color:var(--muted);padding:4px 0;border-bottom:2px solid transparent}
.nav a:hover{color:var(--ink)}
.nav a[aria-current]{color:var(--ink);border-bottom-color:var(--blaze)}
main{padding:0 0 80px}
.lede{font-size:1.25rem;line-height:1.55;color:var(--muted);max-width:60ch}
/* hero */
.hero{position:relative;isolation:isolate;padding:84px 0 72px;border-bottom:1px solid var(--line);background:var(--night)}
.hero .bg{position:absolute;inset:0;z-index:-2;background-size:cover;background-position:center;filter:saturate(.8) brightness(.55)}
.hero:after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,rgba(12,19,14,.96) 0%,rgba(12,19,14,.82) 45%,rgba(12,19,14,.35) 100%),repeating-linear-gradient(0deg,transparent 0 3px,rgba(0,0,0,.18) 3px 4px)}
.hero-grid{display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center}
.hud{text-transform:uppercase;position:absolute;font-size:.75rem;color:var(--khaki);opacity:.8}
.hud.tl{top:18px;left:20px}.hud.tr{top:18px;right:20px;text-align:right}
.hero .lede{color:#C9D0BC}
.page-hero{padding:64px 0 48px}
.page-hero h1{font-size:clamp(2.1rem,5.4vw,3.5rem);max-width:20ch}
/* range card */
.card{position:relative;background:rgba(21,33,26,.88);border:1px solid var(--line);padding:22px 22px 14px;backdrop-filter:blur(4px)}
.card:before,.card:after{content:"";position:absolute;width:18px;height:18px;border:2px solid var(--blaze)}
.card:before{top:-2px;left:-2px;border-right:0;border-bottom:0}.card:after{bottom:-2px;right:-2px;border-left:0;border-top:0}
.card-h{display:flex;justify-content:space-between;font-family:"Share Tech Mono",monospace;font-size:.78rem;letter-spacing:.1em;color:var(--signal);border-bottom:1px dashed var(--line);padding-bottom:10px;margin-bottom:4px}
.rules{list-style:none;margin:0;padding:0}
.rules li{display:grid;grid-template-columns:3.4rem 1fr;gap:12px;padding:14px 0;border-bottom:1px solid var(--line);max-width:none}
.rules li:last-child{border-bottom:0}
.rules .rule-n{font-size:1.7rem;line-height:1;color:var(--blaze);padding-top:2px}
.rules b{display:block;font-size:1.12rem;line-height:1.2;margin-bottom:4px;letter-spacing:.03em}
.rules div span{color:var(--muted);font-size:.98rem;line-height:1.5}
.rules-cap{font-size:.9rem;color:var(--muted);margin:12px 0 0}
.btn{display:inline-block;font-weight:700;font-size:1.05rem;padding:13px 22px;text-decoration:none;background:var(--blaze);color:#120A02;margin:10px 10px 0 0;clip-path:polygon(10px 0,100% 0,100% calc(100% - 10px),calc(100% - 10px) 100%,0 100%,0 10px);transition:background .15s}
.btn:hover{color:#120A02;background:var(--blaze-ink)}
.btn.alt{background:transparent;color:var(--ink);box-shadow:inset 0 0 0 2px var(--khaki);clip-path:none}
.btn.alt:hover{color:var(--blaze-ink);box-shadow:inset 0 0 0 2px var(--blaze-ink)}
/* stats strip */
.strip{display:grid;grid-template-columns:repeat(4,1fr);border-bottom:1px solid var(--line);background:url("CAMO") 0 0/240px}
.strip div{padding:22px 20px;background:rgba(12,19,14,.86);border-right:1px solid var(--line)}
.strip div:last-child{border-right:0}
.strip b{display:block;font-family:"Saira Stencil One",sans-serif;font-weight:400;font-size:2rem;color:var(--khaki);line-height:1.1}
.strip span{font-size:.92rem;color:var(--muted)}
/* guides */
.sec-h{display:flex;justify-content:space-between;align-items:end;gap:16px;flex-wrap:wrap}
.guides{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:16px;margin-top:18px}
.guides a,.post-card{position:relative;display:flex;flex-direction:column;text-decoration:none;background:var(--panel);border:1px solid var(--line);overflow:hidden;transition:transform .15s,border-color .15s}
.guides a:hover,.post-card:hover{transform:translateY(-3px);border-color:var(--olive)}
.guides img,.post-card img{display:block;width:100%;height:auto;aspect-ratio:16/9;object-fit:cover;filter:saturate(.8) contrast(1.05)}
.guides .t,.post-card .t{padding:16px 18px 18px}
.guides .n{position:absolute;top:10px;left:10px;font-family:"Share Tech Mono",monospace;font-size:.75rem;background:rgba(12,19,14,.85);color:var(--signal);padding:3px 8px;letter-spacing:.1em}
.guides b,.post-card b{display:block;font-size:1.3rem;line-height:1.15;margin-bottom:4px}
.guides span,.post-card span{color:var(--muted);font-size:.98rem;line-height:1.5}
.guides a:hover b,.post-card:hover b{color:var(--blaze-ink)}
.meta{font-size:.75rem;color:var(--signal);text-transform:uppercase;display:block;margin-bottom:6px}
/* partner */
.partner{position:relative;margin-top:64px;padding:30px;background:linear-gradient(135deg,rgba(21,33,26,.97),rgba(16,25,18,.93)),url("CAMO") 0 0/240px;border:1px solid var(--olive)}
.partner:before{content:"SPONSORED // TRAINING PARTNER";position:absolute;top:-11px;left:22px;background:var(--bg);padding:0 8px;font-family:"Share Tech Mono",monospace;font-size:.72rem;letter-spacing:.12em;color:var(--signal)}
.partner h2{margin-top:0}
.partner-grid{display:grid;grid-template-columns:1.3fr 1fr;gap:28px;align-items:start}
.small{font-size:.9rem;color:var(--muted)}
.bnr{display:block;margin:6px 0 4px;max-width:100%}.bnr img{display:block;max-width:100%;height:auto;border:1px solid var(--line)}
/* articles */
.article-wrap{display:grid;grid-template-columns:minmax(0,720px) 1fr;gap:56px}
.article ul,.article ol{padding-left:1.3em}
.article li{margin:.4em 0}
.article li::marker{color:var(--blaze)}
.article ol li::marker{font-family:"Share Tech Mono",monospace}
.article b{color:#F3F1E4}
.figure{margin:28px 0;border:1px solid var(--line);background:var(--panel)}
.figure img{display:block;width:100%;height:auto;aspect-ratio:16/8;object-fit:cover;filter:saturate(.85)}
.figure figcaption{font-family:"Share Tech Mono",monospace;font-size:.75rem;letter-spacing:.08em;color:var(--muted);padding:8px 12px}
.note{border-left:4px solid var(--blaze);background:var(--panel);padding:12px 16px;margin:26px 0;color:var(--muted)}
.aside{position:sticky;top:96px;align-self:start;margin-top:8px}
.aside .card{padding:18px}
.aside h3{margin:6px 0 10px;font-size:1.1rem}
.aside ol{margin:0;padding-left:1.2em;font-size:.95rem;color:var(--muted)}
.faq details{border:1px solid var(--line);background:var(--panel);margin:10px 0;padding:0 16px}
.faq summary{cursor:pointer;padding:14px 0;font-weight:600;list-style:none}
.faq summary::-webkit-details-marker{display:none}
.faq summary:before{content:"+ ";color:var(--blaze);font-family:"Share Tech Mono",monospace}
.faq details[open] summary:before{content:"– "}
.faq details p{margin:0 0 14px;color:var(--muted)}
.crumbs{font-family:'Share Tech Mono',monospace;font-size:.8rem;letter-spacing:.06em;color:var(--muted);margin-bottom:18px}.crumbs a{text-decoration:none}.crumbs a:hover{color:var(--blaze-ink)}
.quick{border:1px solid var(--olive);border-left:4px solid var(--blaze);background:var(--panel2);padding:16px 18px;margin:0 0 28px}.quick p{margin:0 0 6px}.quick .small{margin:0}
footer{border-top:1px solid var(--line);padding:0 0 40px;font-size:.95rem;color:var(--muted);background:var(--night)}
footer:before{content:"";display:block;height:10px;background:url("CAMO") 0 0/240px;margin-bottom:28px}
footer .wrap{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}
footer nav{display:flex;gap:16px;flex-wrap:wrap}
@media (max-width:900px){.hero-grid,.partner-grid,.article-wrap{grid-template-columns:minmax(0,1fr);gap:28px}.aside{position:static;order:-1}.hero{padding:64px 0 48px}.strip{grid-template-columns:repeat(2,1fr)}.strip div:nth-child(2){border-right:0}.hud.tr{display:none}}
@media (max-width:520px){.nav{gap:2px 14px}.nav a{font-size:.92rem}.card{padding:18px 16px 10px}.partner{padding:24px 18px}}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
""".replace('CAMO',CAMO)
NAV=[('/choose-a-class/','Choose a class'),('/first-class/','Your first class'),('/safety-storage/','Safety & storage'),('/self-defense-basics/','Self-defense'),('/la-orange-county/','LA & OC'),('/blog/','Blog')]
FOOT=[('/about/','About'),('/affiliate-disclosure/','Affiliate disclosure'),('/privacy/','Privacy'),('/terms/','Terms')]
def page(path,title,desc,body,schema=None,img=None):
    cur=lambda h:' aria-current="page"' if (h==path or (h=='/blog/' and path.startswith('/blog/'))) else ''
    nav=''.join(f'<a href="{h}"{cur(h)}>{t}</a>' for h,t in NAV)
    foot=''.join(f'<a href="{h}">{t}</a>' for h,t in FOOT)
    url=DOM+path
    schemas=schema if isinstance(schema,list) else ([schema] if schema else [])
    sch=''.join(f'<script type="application/ld+json">{json.dumps(s)}</script>' for s in schemas)
    og=IMG(PH[img],1200,630) if img else DOM+'/og-image.jpg'
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:type" content="website"><meta name="twitter:card" content="summary_large_image"><meta property="og:image" content="{og}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><meta name="theme-color" content="#0C130E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link rel="preconnect" href="https://images.unsplash.com">
<link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700&family=Barlow:wght@400;500;600&family=Saira+Stencil+One&family=Share+Tech+Mono&display=swap" rel="stylesheet">
<link rel="alternate" type="application/rss+xml" title="FirearmSafety.us Blog" href="/blog/feed.xml"><link rel="stylesheet" href="/styles.css">{sch}</head><body><a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="wrap"><a class="brand" href="/"><i aria-hidden="true"></i><span>FirearmSafety<em>.us</em></span></a><nav class="nav" aria-label="Main">{nav}</nav></div></header>
<main id="main">{body}</main>
<footer><div class="wrap"><p>FirearmSafety.us is an independent safety-education guide. It does not sell firearms, ammunition or accessories.<br><span class="small">Photography via Unsplash.</span></p><nav aria-label="Footer">{foot}</nav></div></footer>
</body></html>'''
def write(path,html):
    d=OUT+path; os.makedirs(d,exist_ok=True); global _bi
    _bi=globals().get('_bi',-1)+1
    open(d+'index.html','w').write(html.replace('{UDT}',UDT).replace('{BANNER}',banner(_bi)))
PARTNER=f'''<section class="partner" aria-labelledby="p-title"><div class="partner-grid"><div><h2 id="p-title">Find a class with United Defense Tactical</h2>
<p>United Defense Tactical teaches firearms safety, shooting fundamentals and self-defense classes in Southern California, with instructors working in Los Angeles and Orange County.</p>
<a class="btn" href="{UDT}" target="_blank" rel="sponsored nofollow noopener">See classes and dates</a>
<p class="small">Sponsored link. If you book through it, we may earn a commission at no extra cost to you. <a href="/affiliate-disclosure/">How we work with partners</a></p></div><div>{{BANNER}}</div></div></section>'''
def ASIDE(points):
    li=''.join(f'<li>{p}</li>' for p in points)
    return f'<aside class="aside"><div class="card"><div class="card-h"><span>FIELD NOTES</span><span>// BRIEF</span></div><h3>Key points</h3><ol>{li}</ol></div></aside>'
def ART(h1,lede,inner,img='canopy',kicker='Field manual',points=None,cap=''):
    hero=f'<section class="hero page-hero"><div class="bg" style="background-image:url({IMG(PH[img],1600)})"></div><span class="hud tl">FIREARMSAFETY.US // {kicker}</span><div class="wrap"><span class="kicker">{kicker}</span><h1>{h1}</h1><p class="lede">{lede}</p></div></section>'
    side=ASIDE(points) if points else '<div></div>'
    return hero+f'<div class="wrap"><div class="article-wrap" style="margin-top:40px"><article class="article">{inner}</article>{side}</div>'+PARTNER+'</div>'
def FIG(img,cap): return f'<figure class="figure"><img src="{IMG(PH[img],1100)}" alt="{cap}" loading="lazy" decoding="async" width="1100" height="550"><figcaption>{cap.upper()}</figcaption></figure>'
def FAQ(qs):
    html='<section class="faq"><h2>Common questions</h2>'+''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in qs)+'</section>'
    sch={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in qs]}
    return html,sch
def artschema(t,d,p,img=None):
    s={"@context":"https://schema.org","@type":"Article","headline":t,"description":d,"mainEntityOfPage":DOM+p,"datePublished":TODAY,"dateModified":TODAY,"author":{"@type":"Organization","name":"FirearmSafety.us"},"publisher":{"@type":"Organization","name":"FirearmSafety.us","url":DOM}}
    if img: s["image"]=IMG(PH[img],1200,630).replace('&amp;','&')
    return s

# Home
rules=[('Treat every firearm as if it is loaded.','Even when someone has just shown you it is empty. Check it yourself, every time.'),
('Never point the muzzle at anything you are not willing to destroy.','Keep it pointed in a safe direction while you hold it, hand it over or put it down.'),
('Keep your finger off the trigger until your sights are on target and you have decided to shoot.','Rest it straight along the frame instead.'),
('Be sure of your target and what is beyond it.','A shot can pass through or miss. Know where it will stop.')]
rl=''.join(f'<li><span class="rule-n" aria-hidden="true">0{i+1}</span><div><b>{a}</b><span>{b}</span></div></li>' for i,(a,b) in enumerate(rules))
guides=[('/choose-a-class/','Choose a class','What to compare between instructors, class types and ranges.','instructor'),
('/first-class/','Your first class','What happens on the day, what to bring and what to wear.','woman'),
('/safety-storage/','Safety &amp; storage','Locking, storing and transporting firearms at home and in the car.','leaves'),
('/self-defense-basics/','Self-defense basics','Awareness, avoidance and de-escalation come before any tool.','path'),
('/la-orange-county/','LA &amp; Orange County','Training in Southern California and the state rules to know first.','bridge')]
gl=''.join(f'<a href="{h}"><img src="{IMG(PH[im],640,360)}" alt="" loading="lazy" decoding="async" width="640" height="360"><span class="n">GUIDE 0{i+1}</span><div class="t"><b>{t}</b><span>{d}</span></div></a>' for i,(h,t,d,im) in enumerate(guides))

DOJ='<a href="https://oag.ca.gov/firearms" rel="noopener" target="_blank">California Department of Justice</a>'
POSTS=[
('california-firearm-safety-certificate','California Firearm Safety Certificate (FSC): how the test works','What the California FSC test covers, how many questions you need to pass, what it costs and how long it lasts.','target','California law',
 ['30 questions, 23 correct to pass (75%).','The fee is $25.','The certificate is valid for five years.','Study the official DOJ guide first.'],
 '''<p>If you want to buy a firearm in California, the first step is usually the Firearm Safety Certificate, or FSC. It is a short written test on safe handling and basic law. It is not a shooting test, but it is a good test of whether you have learned the basics.</p>
<h2>The numbers</h2><ul>
<li><b>Questions:</b> 30, multiple choice and true/false.</li>
<li><b>Pass mark:</b> at least 75%, which means 23 correct answers.</li>
<li><b>Fee:</b> $25 for the test and the certificate.</li>
<li><b>Valid for:</b> five years from the date it is issued.</li></ul>
<p>These figures come from the California Department of Justice's own FSC FAQ. Check it before you go in case anything has changed.</p>
<h2>Where you take it</h2><p>The test is given by DOJ-certified instructors, most often at licensed firearm dealers. Bring a government-issued photo ID. If you fail, you can retake it, but there is a short wait before you can try again and you pay again.</p>
<h2>What it covers</h2><p>The DOJ publishes a free study guide. Expect questions on:</p><ul>
<li>The basic safety rules and safe handling.</li>
<li>How to store firearms safely, especially around children.</li>
<li>Carrying and transporting firearms legally in California.</li>
<li>Who is prohibited from owning firearms.</li>
<li>Responsibilities of an owner after a purchase.</li></ul>
<h2>Other rules to expect at the counter</h2><p>California also has a waiting period between purchase and pickup (currently 10 days) and age minimums (21 for most purchases). A handgun purchase also needs a safe-handling demonstration with the dealer. Rules here change often, so confirm the current list with the '''+DOJ+'''.</p>
<h2>How to prepare</h2><p>Read the study guide twice, and take a beginner safety class before the test. A good instructor will explain the reasons behind the rules, which makes the questions easy. You will also leave knowing how to handle a firearm safely, which the test alone cannot teach.</p>''',
 [('How many questions are on the California FSC test?','30 questions. You need at least 23 correct (75%) to pass.'),('How much does the FSC cost?','$25 for the test and certificate, according to the California DOJ.'),('How long is an FSC valid?','Five years from the date it is issued.')]),
('california-safe-storage-law-sb-53','California safe storage law (SB 53): what changed in 2026','How California\'s SB 53 secure storage rule works at home, what counts as secure storage and practical ways to comply.','leaves','Storage',
 ['In force since January 1, 2026.','Unattended firearms at home must be locked or disabled.','First two offenses: infractions up to $500.','A certified safe or lock device counts.'],
 '''<p>California's Senate Bill 53 took effect on January 1, 2026. It extends the state's older child-access rules to every home. In short, if a firearm in a residence is not being carried or kept under the control of a lawful user, it has to be stored securely.</p>
<h2>What counts as secure storage</h2><p>The law defines it as being kept in, locked by, or disabled with a <b>certified firearm safety device</b> or a <b>secure gun safe</b>. In practice, that means one of these:</p><ul>
<li>A DOJ-approved gun safe or lockbox.</li>
<li>A certified cable lock or trigger lock fitted so the firearm cannot fire.</li></ul>
<p>Hiding a firearm in a drawer, a closet or under a mattress is not secure storage.</p>
<h2>Penalties</h2><p>First and second violations are infractions with fines of up to $500. Later violations can be charged as misdemeanors. Separate, more serious laws apply if a child or prohibited person gets hold of a firearm.</p>'''+FIG('leaves','Store it locked. Keep keys and codes under your control.')+'''<h2>A simple storage plan</h2><ol>
<li><b>Choose the container</b> for how you use the firearm: a quick-access lockbox for a home-defense handgun, a larger safe for long guns.</li>
<li><b>Unload before storing</b> unless you have a considered reason not to, and lock ammunition separately when you can.</li>
<li><b>Control access.</b> Do not share codes with children, and do not hide keys where they can be found.</li>
<li><b>Practice opening it</b> in the dark and under pressure so secure storage does not feel like a trade-off.</li>
<li><b>Re-check when guests stay</b> or when life changes, such as a new baby or a teenager in the house.</li></ol>
<p class="note">This is general information, not legal advice. Read the current rules on the '''+DOJ+''' website and ask a qualified attorney about your own situation.</p>''',
 [('When did SB 53 take effect?','January 1, 2026.'),('What is the penalty for not storing a firearm securely in California?','The first and second offenses are infractions with fines of up to $500. Later offenses can be misdemeanors.'),('Does a cable lock count as secure storage?','A certified firearm safety device, such as an approved cable lock fitted so the firearm cannot fire, meets the definition.')]),
('california-ccw-training-requirements','California CCW training: what the 16-hour course covers','What to expect from California\'s concealed carry (CCW) training under SB 2: hours, live fire, the application process and renewal.','instructor','Carry permits',
 ['At least 16 hours of initial training.','Includes a live-fire qualification.','Apply through your county sheriff or city police.','Renewal needs a shorter refresher course.'],
 '''<p>Since SB 2 took effect in 2024, getting a concealed carry weapon (CCW) license in California involves more training than before. If you are in Los Angeles or Orange County, this is the outline to expect.</p>
<h2>Who issues the license</h2><p>Your county sheriff or, in some cities, your city police chief. In Southern California that usually means the LA County Sheriff's Department, the LAPD for City of LA residents, or the Orange County Sheriff's Department. Each agency publishes its own steps, fees and list of approved instructors.</p>
<h2>The training</h2><ul>
<li><b>Hours:</b> at least 16 hours for a first license, with a shorter refresher course (8 hours) for renewal.</li>
<li><b>Classroom topics:</b> firearm safety, handling and storage, use-of-force law, where carrying is prohibited, and how to deal with police while carrying.</li>
<li><b>Live fire:</b> a qualification course with each firearm you list on the license, scored by the instructor.</li></ul>
<p>Use an instructor your issuing agency accepts. A certificate from someone not on the list can mean taking the course again.</p>'''+FIG('instructor','A qualified instructor runs the line and scores your qualification.')+'''<h2>The rest of the process</h2><ol>
<li>Apply through your agency's portal and pay the first fee.</li>
<li>Complete Live Scan fingerprinting and the background check.</li>
<li>Attend an interview if your agency requires one.</li>
<li>Complete the approved training and qualification.</li>
<li>Pay the remaining fees and collect your license.</li></ol>
<p>Expect the process to take weeks or months, depending on the agency.</p>
<h2>Start with the basics</h2><p>A CCW course assumes you can already handle a firearm safely. If you are new, take a fundamentals class first, such as a <a href="{UDT}" target="_blank" rel="sponsored nofollow noopener">beginner course with United Defense Tactical</a>. You will get far more from the CCW class.</p>
<p class="note">Requirements vary by agency and change over time. Confirm with your sheriff or police department and the '''+DOJ+'''.</p>''',
 [('How many hours of training does a California CCW need?','At least 16 hours for a first license, including live fire, and a shorter refresher course for renewal.'),('Where do I apply for a CCW in Los Angeles or Orange County?','Through your county sheriff, or your city police chief where they issue licenses (for example the LAPD for City of LA residents).')]),
('range-etiquette-first-visit','Range etiquette: your first visit to a shooting range','The commands, rules and habits that keep everyone safe at an indoor or outdoor range, explained for first-timers.','indoor','Range basics',
 ['Read and follow the posted range rules.','"Cease fire" means stop at once.','Keep the muzzle downrange at all times.','Ask staff when unsure. They expect it.'],
 '''<p>Ranges are some of the most rule-bound places you will visit, and that is a good thing. Everyone follows the same small set of habits. Learn them before your first visit and you will feel at home quickly.</p>
<h2>Before you go</h2><ul>
<li>Check whether you need a reservation, a waiver or a range safety briefing.</li>
<li>Transport firearms unloaded and in a case. Do not uncase them until you are at your lane.</li>
<li>Bring eye and ear protection, or plan to rent them.</li>
<li>Wear a crew-neck top, closed-toe shoes and a brimmed cap.</li></ul>
<h2>Range commands</h2><ul>
<li><b>"Cease fire":</b> stop shooting at once, take your finger off the trigger and keep the muzzle downrange. Anyone can call it.</li>
<li><b>"The line is hot":</b> shooting may begin.</li>
<li><b>"The line is cold":</b> firearms are unloaded, actions open and benched. Nobody handles a firearm while people are downrange.</li></ul>'''+FIG('indoor','Muzzle downrange, finger off the trigger until on target.')+'''<h2>At your lane</h2><ol>
<li>Keep the muzzle pointed downrange whenever the firearm is in your hand.</li>
<li>Uncase, load and unload only at the firing line.</li>
<li>If something goes wrong, keep it pointed downrange and call staff. Do not turn around with it.</li>
<li>Pick up only your own brass, and only when the range allows it.</li></ol>
<h2>Courtesy</h2><p>Give neighbors space, do not offer coaching unless asked, and do not handle anyone else's firearm without permission. If you are new, say so. Range staff would much rather answer a question than correct a mistake.</p>
<p>The easiest first visit is with an instructor. A <a href="{UDT}" target="_blank" rel="sponsored nofollow noopener">guided beginner session</a> covers all of this on the day.</p>''',
 [('What does "cease fire" mean at a range?','Stop shooting immediately, take your finger off the trigger and keep the muzzle pointed downrange until told otherwise.'),('Can I bring my own firearm to a public range?','Usually yes. Transport it unloaded and cased, and only uncase it at your lane. Check the range rules first.')]),
('eye-and-ear-protection-guide','Eye and ear protection for shooting: a beginner\'s guide','How to choose shooting glasses and hearing protection, what NRR means, and why indoor ranges call for doubling up.','woman','Gear',
 ['Choose eyewear marked ANSI Z87.1+.','A higher NRR means more noise blocked.','Double up indoors: foam plugs plus muffs.','Electronic muffs let you hear commands.'],
 '''<p>Gunshots are loud enough to cause permanent hearing damage after a single exposure, and hot brass and fragments can hit your eyes. Protection is required at every range, and it is the cheapest safety equipment you will buy.</p>
<h2>Eye protection</h2><ul>
<li>Look for <b>ANSI Z87.1+</b> on the frame. The "+" means it is rated for high-velocity impact.</li>
<li>Wraparound lenses protect the sides. Ejected brass often comes from an angle.</li>
<li>Clear or yellow lenses work indoors, and tinted lenses outdoors.</li>
<li>If you wear prescription glasses, add over-the-glasses safety eyewear unless your lenses are impact-rated.</li></ul>
<h2>Hearing protection and NRR</h2><p>Hearing protection is rated by its <b>Noise Reduction Rating (NRR)</b>, in decibels. Higher means more protection. Foam plugs often reach 29 to 33, and muffs around 22 to 30.</p>'''+FIG('woman','Eyes and ears on before you step onto the line.')+'''<h2>Double up indoors</h2><p>Indoor ranges trap and reflect sound, so many instructors recommend foam plugs and muffs together. Roll each plug tight and let it expand fully in your ear canal. A loose plug does very little.</p>
<h2>Passive or electronic muffs?</h2><p>Passive muffs simply block sound. Electronic muffs let normal speech through and shut down when a shot fires, so you can still hear range commands and your instructor. If you plan to train regularly, electronic muffs are worth buying.</p>
<p>Most beginner classes provide protection or rent it. Ask when you book, for example on the <a href="{UDT}" target="_blank" rel="sponsored nofollow noopener">United Defense Tactical class page</a>.</p>''',
 [('What NRR do I need for shooting?','Use the highest NRR you can wear comfortably. Indoors, combine foam plugs with muffs.'),('Are regular sunglasses OK for shooting?','Only if they are impact-rated. Look for ANSI Z87.1+ on the frame.')]),
('safe-dry-practice-at-home','Safe dry practice at home: a checklist','How to practice grip, sight alignment and trigger control at home with an unloaded firearm, and the routine that keeps it safe.','coach','Practice',
 ['No ammunition in the practice room.','Check the firearm is unloaded, then check again.','Point at a safe backstop the whole time.','Say out loud when practice ends.'],
 '''<p>Dry practice is practicing with an unloaded firearm. It is how most shooters improve between range trips, and it is free. It is only safe when you follow the same routine every time. Most negligent discharges at home happen at the end of a session, when attention drops.</p>
<p class="note">Learn grip and trigger control from a qualified instructor first, then use dry practice to reinforce what you were taught.</p>
<h2>Set up the space</h2><ol>
<li><b>Choose a room</b> and a <b>safe backstop</b> that could stop a round, such as a full bookcase or a ballistic panel on an exterior wall. Not an interior wall with people beyond it.</li>
<li><b>Remove all ammunition</b> from the room. Not on the table, not in a pocket, not in a magazine nearby.</li>
<li><b>Unload and check</b> the firearm: remove the magazine, lock the action open, then look and feel the chamber. Ask a second person to check if you can.</li>
<li><b>Remove distractions:</b> phone on silent, nobody walking through.</li></ol>'''+FIG('coach','Learn the fundamentals in person first. Reinforce them at home.')+'''<h2>During practice</h2><ul>
<li>Keep the muzzle on the backstop the whole time.</li>
<li>Keep sessions short, around 10 to 15 minutes. Focus fades fast.</li>
<li>Work one skill at a time: a smooth trigger press with no sight movement, a consistent grip, or sight alignment.</li>
<li>If anyone enters the room, stop.</li></ul>
<h2>Ending the session</h2><p>Say "practice is over" out loud. Then store the firearm or put it away securely before any ammunition comes back into the room. Do not reload for a "last one".</p>
<h2>Tools that help</h2><p>Inert training rounds (snap caps) and laser training cartridges can help. Store them separately from live ammunition and keep them a distinct color.</p>
<p>To build the fundamentals first, take a <a href="{UDT}" target="_blank" rel="sponsored nofollow noopener">fundamentals class</a> and ask the instructor for a dry practice plan.</p>''',
 [('Is dry fire practice safe?','It is safe when you follow a strict routine: no ammunition in the room, a verified unloaded firearm, a safe backstop and a clear end to the session.'),('How long should dry practice sessions be?','Short, around 10 to 15 minutes, while your focus is sharp.')]),
]
def post_card(slug,t,d,img,tag):
    return f'<a class="post-card" href="/blog/{slug}/"><img src="{IMG(PH[img],640,360)}" alt="" loading="lazy" decoding="async" width="640" height="360"><div class="t"><span class="meta">{tag} // {TODAY}</span><b>{t}</b><span>{d}</span></div></a>'

latest=''.join(post_card(s,t,d,im,tag) for s,t,d,im,tag,*_ in POSTS[:3])
hq=[('Do I need experience to take a firearm safety class?','No. Beginner classes assume no experience. They start with the safety rules and how a firearm works before any live fire.'),
('What should I bring to my first class?','A government-issued photo ID, eye and ear protection unless provided, water, and closed-toe shoes with a crew-neck top.'),
('Do I need a Firearm Safety Certificate in California?','Generally yes, before you can buy a firearm. It is a 30-question test and you need 23 correct to pass.')]
faqh,faqs=FAQ(hq)
home=f"""<section class="hero"><div class="bg" style="background-image:url({IMG(PH['fronds'],1800)})"></div><span class="hud tl">GRID 34.05N / 118.24W // LA-OC SECTOR</span><span class="hud tr">STATUS: SAFETY FIRST<br>OPS: TRAINING</span>
<div class="wrap hero-grid"><div><span class="kicker">Mission brief // Beginners</span><h1>Learn to handle a firearm safely, from your first class on.</h1>
<p class="lede">A plain-language guide for adults who are new to firearms or self-defense training in Southern California: how to choose a class, what to expect, and how to stay safe at home.</p>
<a class="btn" href="/choose-a-class/">Start with choosing a class</a><a class="btn alt" href="/first-class/">What your first class is like</a></div>
<div class="card"><div class="card-h"><span>RANGE CARD // 4 RULES</span><span>MEMORIZE</span></div><ol class="rules" aria-label="The four rules of firearm safety">{rl}</ol><p class="rules-cap">Every good class starts with these four rules. Learn them before you touch a firearm.</p></div></div></section>
<section class="strip" aria-label="California quick facts"><div><b>30 Q</b><span>FSC test, 23 correct to pass</span></div><div><b>10 DAYS</b><span>CA waiting period before pickup</span></div><div><b>16 HRS</b><span>Minimum CCW training (SB 2)</span></div><div><b>2026</b><span>Secure home storage law (SB 53)</span></div></section>
<div class="wrap"><div class="sec-h"><h2>Field guides</h2><span class="kicker">05 modules</span></div><div class="guides">{gl}</div>
<div class="sec-h"><h2>Latest from the blog</h2><a href="/blog/" class="kicker" style="text-decoration:none">All posts &rarr;</a></div><div class="guides">{latest}</div>
<div style="max-width:760px">{faqh}</div>{PARTNER}</div>"""
write('/', page('/','FirearmSafety.us: firearm safety and self-defense training for beginners','A beginner guide to firearm safety and self-defense training in Southern California: choosing a class, your first lesson, safe storage and state rules.',home,
 [{"@context":"https://schema.org","@type":"WebSite","name":"FirearmSafety.us","url":DOM},faqs],img='fronds'))

P={}
P['/choose-a-class/']=('How to choose a firearm safety class','What to compare between instructors, class types and ranges before you book a beginner firearm safety class.',
 ART('How to choose a firearm safety class','The right first class is small, unhurried and run by an instructor who spends more time on safety than on shooting.',
 '''<h2>Start with the class type</h2><ul class="check">
<li><b>Intro to firearm safety:</b> classroom-first. You learn the safety rules, how a firearm works and how to unload it, often before any live fire.</li>
<li><b>Basic pistol or fundamentals:</b> safety plus grip, stance, sight alignment and trigger control, with supervised live fire.</li>
<li><b>Private lesson:</b> one instructor, one student. Useful if you are nervous or want to go at your own pace.</li>
<li><b>Self-defense courses:</b> come after the basics. They should cover awareness and the law, not only shooting.</li></ul>
<h2>Questions to ask before you book</h2><p>Use these when you compare instructors, including the <a href="{UDT}" target="_blank" rel="sponsored nofollow noopener">United Defense Tactical class list</a>.</p><ul class="check">
<li>Who teaches the class, and what certifications do they hold?</li>
<li>How many students are there per instructor on the firing line?</li>
<li>Can I rent or borrow a firearm, eye and ear protection, or do I bring my own?</li>
<li>How much of the class is classroom time and how much is range time?</li>
<li>What is the refund or rescheduling policy?</li></ul>
<h2>Signs of a good instructor</h2><p>They repeat the safety rules often, correct mistakes calmly, and stop the line the moment anything looks unsafe. They are happy to answer basic questions. A class that rushes to live fire or treats safety as a formality is not the right place to start.</p>
<p class="note">Requirements to buy or own a firearm vary by state. In California, check the current rules with the <a href="https://oag.ca.gov/firearms" rel="noopener" target="_blank">California Department of Justice</a>.</p>''','instructor','Field manual',['Start with an intro or fundamentals class.','Ask about students per instructor.','Good instructors stop the line for anything unsafe.','Check California DOJ rules before buying.']))
P['/first-class/']=('Your first firearm safety class: what to expect','What happens at a beginner firearm class, what to bring, what to wear and how the day usually runs.',
 ART('Your first firearm safety class','Most beginner classes follow the same shape: safety briefing, classroom basics, then supervised range time. Nobody expects you to know anything yet.',
 '''<h2>How the day usually runs</h2><ol>
<li><b>Check-in and safety briefing.</b> You will sign a waiver and hear the range rules and the four safety rules.</li>
<li><b>Classroom.</b> How the firearm works, how to load and unload it, and how to clear a malfunction.</li>
<li><b>Dry practice.</b> Grip, stance and trigger control with an unloaded firearm or a training replica.</li>
<li><b>Supervised live fire.</b> A few rounds at a time at a close target, with the instructor beside you.</li>
<li><b>Debrief.</b> What went well, what to practise, and next steps.</li></ol>
<h2>What to bring</h2><ul class="check"><li>A government-issued photo ID.</li><li>Eye and ear protection, unless the class provides it.</li><li>Water and a snack for longer classes.</li><li>Any paperwork the instructor sent you.</li></ul>
<h2>What to wear</h2><p>Closed-toe shoes, a crew-neck top (hot brass can fall into a low neckline), and a cap with a brim. Avoid loose, baggy clothing.</p>
<h2>If you feel nervous</h2><p>That is normal and useful: it keeps you careful. Tell the instructor at the start. You can always pause, ask questions, or skip the live-fire part and come back another day.</p>''','woman','First mission',['Briefing, classroom, dry practice, then live fire.','Bring photo ID, eye and ear protection.','Wear a crew-neck top and closed-toe shoes.','Nervous is normal. Tell your instructor.']))
P['/safety-storage/']=('Safe firearm storage and transport at home','How to lock, store and transport firearms safely, especially in homes with children or visitors.',
 ART('Safe storage and transport','Most firearm accidents at home happen when someone who should not have access finds an unsecured gun. Storage is part of safety, not an extra.',
 '''<h2>Storage at home</h2><ul class="check">
<li><b>Lock it up.</b> Use a gun safe, lockbox or locking device. A locked container is the safest option.</li>
<li><b>Store ammunition separately</b> when you can, also locked.</li>
<li><b>Control the keys and codes.</b> Do not hide keys where children or visitors can find them.</li>
<li><b>Unload before storing</b>, unless you have a specific, well-considered reason and secure storage.</li></ul>
<h2>Children and visitors</h2><p>Children are curious and can find hiding places adults think are secret. Teach them that if they ever see a gun, they should not touch it, leave the area and tell an adult. When visitors stay over, check that everything is locked away.</p>
<h2>Transport</h2><p>Carry firearms unloaded and in a locked container, and follow your state's transport rules. Rules differ between states and can change, so check before you travel.</p>
<p class="note">California has specific storage and transport laws. Read the current requirements on the <a href="https://oag.ca.gov/firearms" rel="noopener" target="_blank">California Department of Justice firearms pages</a>.</p>''','leaves','Secure storage',['Lock it: safe, lockbox or certified lock.','Store ammunition separately.','Control keys and codes.','California SB 53 applies from 2026.']))
P['/self-defense-basics/']=('Self-defense basics: awareness, avoidance and de-escalation','The foundations of personal safety that come before any self-defense tool: awareness, avoidance, de-escalation and knowing the law.',
 ART('Self-defense basics','Good self-defense training spends most of its time on not needing to defend yourself at all.',
 '''<h2>Awareness</h2><p>Notice your surroundings: exits, who is nearby, what feels out of place. Put the phone away in parking lots and at transit stops, and trust the feeling that something is wrong.</p>
<h2>Avoidance</h2><p>The best outcome is not being there. Change direction, cross the street, go into a busy shop, or leave early. Plan routes and travel with others when you can.</p>
<h2>De-escalation</h2><p>Keep distance, keep your hands visible, speak calmly and give the other person a way out. Property can be replaced. Walking away is a win.</p>
<h2>Know the law</h2><p>Self-defense law is specific and varies by state. A good course explains when force is and is not lawful. For advice about your situation, talk to a qualified attorney.</p>
<h2>Where firearm training fits</h2><p>If you choose to own a firearm for home defense, safety and regular practice with a qualified instructor matter more than the equipment. Start with a <a href="{UDT}" target="_blank" rel="sponsored nofollow noopener">beginner safety class</a>.</p>''','path','Situational awareness',['Awareness first.','Avoid trouble: leave, cross, go somewhere busy.','De-escalate: distance, calm voice, a way out.','Know your state\'s self-defense law.']))
P['/la-orange-county/']=('Firearm safety training in Los Angeles and Orange County','Training options in Southern California and the California rules beginners should know before buying or carrying a firearm.',
 ART('Training in Los Angeles and Orange County','Southern California has indoor and outdoor ranges and many private instructors. California also has some of the most detailed firearm rules in the US, so start with the basics.',
 '''<h2>Rules to know first in California</h2><ul class="check">
<li><b>Firearm Safety Certificate (FSC):</b> generally required before you can buy a firearm in California. The test covers basic safety and law.</li>
<li><b>Waiting period:</b> California requires a waiting period before a purchased firearm can be picked up.</li>
<li><b>Carry permits:</b> carrying a concealed firearm needs a county-issued license, which includes required training.</li></ul>
<p class="note">Rules change. Always confirm the current requirements with the <a href="https://oag.ca.gov/firearms" rel="noopener" target="_blank">California Department of Justice</a> and your county sheriff or police department.</p>
<h2>Choosing where to train</h2><p>Look for classes close enough that you will go back for practice. Ask about class size, whether rentals and protective gear are available, and whether the instructor offers a follow-up session.</p>
<h2>Next steps</h2><p>Read <a href="/choose-a-class/">how to choose a class</a> and <a href="/first-class/">what your first class is like</a>, then <a href="{UDT}" target="_blank" rel="sponsored nofollow noopener">book a beginner session</a>.</p>''','bridge','Sector: LA &amp; OC',['FSC: 30 questions, 23 to pass, $25, valid 5 years.','10-day waiting period before pickup.','CCW: at least 16 hours of training plus live fire.','Confirm current rules with the CA DOJ.']))
PIMG={'/choose-a-class/':'instructor','/first-class/':'woman','/safety-storage/':'leaves','/self-defense-basics/':'path','/la-orange-county/':'bridge'}
for p,(t,d,b) in P.items(): write(p,page(p,t+' | FirearmSafety.us',d,b,artschema(t,d,p,PIMG[p]),img=PIMG[p]))

legal={
'/about/':('About FirearmSafety.us','Who runs FirearmSafety.us and how we write our guides.','<article class="article"><h1>About FirearmSafety.us</h1><p class="lede">FirearmSafety.us is an independent guide for adults who are new to firearm safety and self-defense training.</p><p>We focus on safety, choosing qualified instructors and following the law. We do not sell firearms, ammunition or accessories, and we do not publish tactical instruction. For legal requirements we link to official sources instead of interpreting them.</p><p>FirearmSafety.us is published by GetServices.ai. Questions or corrections: <a href="mailto:hello@getservices.ai">hello@getservices.ai</a>.</p></article>'),
'/affiliate-disclosure/':('Affiliate disclosure','How FirearmSafety.us works with partners and earns commission.','<article class="article"><h1>Affiliate disclosure</h1><p class="lede">Some links on this site are affiliate links. If you book a class through them, we may earn a commission at no extra cost to you.</p><p>Our current partner is United Defense Tactical, through the Awin affiliate network. Partner links are marked as sponsored. Commission never changes our safety advice.</p></article>'),
'/privacy/':('Privacy policy','How FirearmSafety.us handles your data.','<article class="article"><h1>Privacy policy</h1><p class="lede">We collect as little as possible.</p><p>This site has no accounts or forms. It loads fonts from Google Fonts, which receives your IP address when the fonts load. When you click a partner link, the Awin network and the partner may set cookies to track the referral. See their privacy policies for details. Contact: <a href="mailto:hello@getservices.ai">hello@getservices.ai</a>.</p></article>'),
'/terms/':('Terms of use','Terms for using FirearmSafety.us.','<article class="article"><h1>Terms of use</h1><p class="lede">FirearmSafety.us is for general education only.</p><p>It is not legal advice and is not a substitute for in-person instruction from a qualified instructor. Laws vary and change, so check current requirements with official sources. You are responsible for following the law and range rules. Content may change without notice.</p></article>'),
}
cards=''.join(post_card(s,t,d,im,tag) for s,t,d,im,tag,*_ in POSTS)
blogbody=f"""<section class="hero page-hero"><div class="bg" style="background-image:url({IMG(PH['canopy'],1600)})"></div><span class="hud tl">FIREARMSAFETY.US // INTEL</span><div class="wrap"><span class="kicker">Intel // Blog</span><h1>Blog</h1><p class="lede">Practical guides on firearm safety, California rules and training. New to all this? Start with <a href="/choose-a-class/">choosing a class</a> or <a href="/first-class/">what your first class is like</a>.</p></div></section><div class="wrap" style="margin-top:40px"><div class="guides">{cards}</div>{PARTNER}</div>"""
write('/blog/', page('/blog/','Blog | FirearmSafety.us','Guides and articles on firearm safety, California rules and training for beginners.',blogbody,
 {"@context":"https://schema.org","@type":"Blog","name":"FirearmSafety.us Blog","url":DOM+'/blog/',"blogPost":[{"@type":"BlogPosting","headline":t,"url":f"{DOM}/blog/{s}/","datePublished":TODAY} for s,t,*_ in POSTS]},img='canopy'))
QA={
'california-firearm-safety-certificate':'To buy a firearm in California you usually need a Firearm Safety Certificate (FSC). The written test has 30 questions and you need 23 correct (75%) to pass. It costs $25, is given by DOJ-certified instructors (usually at licensed dealers) and the certificate is valid for five years.',
'california-safe-storage-law-sb-53':'Since January 1, 2026, California SB 53 requires a firearm at home that is not being carried or under a lawful user\'s control to be kept in a secure gun safe, or locked or disabled with a certified firearm safety device. First and second violations are infractions with fines of up to $500.',
'california-ccw-training-requirements':'A first California CCW license needs at least 16 hours of approved training, including a live-fire qualification with each firearm on the license. Renewals need a shorter refresher (8 hours). You apply through your county sheriff or, in some cities, the police chief.',
'range-etiquette-first-visit':'At a shooting range, follow the posted rules, keep the muzzle pointed downrange, keep your finger off the trigger until you are on target, and stop at once when anyone calls "cease fire". Never handle a firearm while the line is cold and people are downrange.',
'eye-and-ear-protection-guide':'For shooting, wear eyewear marked ANSI Z87.1+ and hearing protection with the highest Noise Reduction Rating (NRR) you can wear comfortably. At indoor ranges, wear foam earplugs and earmuffs together. Electronic muffs let you hear range commands.',
'safe-dry-practice-at-home':'Safe dry practice means practicing with a verified unloaded firearm, with no ammunition in the room, pointed at a backstop that could stop a round, in short sessions of 10 to 15 minutes. Say out loud when practice ends and store the firearm before ammunition returns to the room.',
}
for s,t,d,im,tag,pts,inner,qs in POSTS:
    p=f'/blog/{s}/'; fh,fs=FAQ(qs)
    crumbs=f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> / <a href="/blog/">Blog</a> / <span>{tag}</span></nav>'
    qa=f'<div class="quick" id="quick-answer"><span class="kicker">Quick answer</span><p>{QA[s]}</p><p class="small">Updated <time datetime="{TODAY}">{TODAY}</time> · By FirearmSafety.us editors · Sources linked in the article</p></div>'
    rel=[x for x in POSTS if x[0]!=s][:3]
    related='<section><h2>Related guides</h2><div class="guides">'+''.join(post_card(r[0],r[1],r[2],r[3],r[4]) for r in rel)+'</div></section>'
    bc={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Home","item":DOM+'/'},{"@type":"ListItem","position":2,"name":"Blog","item":DOM+'/blog/'},{"@type":"ListItem","position":3,"name":t,"item":DOM+p}]}
    a=artschema(t,d,p,im); a["@type"]="BlogPosting"; a["articleSection"]=tag; a["abstract"]=QA[s]; a["inLanguage"]="en-US"
    a["speakable"]={"@type":"SpeakableSpecification","cssSelector":["#quick-answer p","h1"]}
    write(p,page(p,t+' | FirearmSafety.us',d,ART(t,d,crumbs+qa+inner+fh+related,im,tag,pts),[a,bc,fs],img=im))
SIMPLE=lambda b:f'<div class="wrap page-hero" style="max-width:820px">{b}</div>'
for p,(t,d,b) in legal.items(): write(p,page(p,t+' | FirearmSafety.us',d,SIMPLE(b.replace('<article class="article">','<article class="article"><span class="kicker">Standard operating info</span>'))))
open(OUT+'/404.html','w').write(page('/404/','Page not found | FirearmSafety.us','This page does not exist.',SIMPLE('<span class="kicker">404 // Off the map</span><h1>This page does not exist.</h1><p class="lede">It may have moved. Go to the <a href="/">home page</a> or start with <a href="/choose-a-class/">choosing a class</a>.</p>')))
open(OUT+'/styles.css','w').write(CSS.strip())
open(OUT+'/CNAME','w').write('firearmsafety.us\n')
open(OUT+'/favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#1B2A20"/><circle cx="16" cy="16" r="8" fill="none" stroke="#F07A1E" stroke-width="2.5"/><path d="M16 4v24M4 16h24" stroke="#F07A1E" stroke-width="2.5"/></svg>')
paths=['/']+list(P)+['/blog/']+[f'/blog/{x[0]}/' for x in POSTS]+list(legal)
def pri(p): return '1.0' if p=='/' else ('0.9' if p in P or p=='/blog/' else ('0.8' if p.startswith('/blog/') else '0.3'))
def freq(p): return 'weekly' if p in ('/','/blog/') else 'monthly'
open(OUT+'/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{DOM}{p}</loc><lastmod>{TODAY}</lastmod><changefreq>{freq(p)}</changefreq><priority>{pri(p)}</priority></url>\n' for p in paths)+'</urlset>\n')
import email.utils,html as _h
rfc=email.utils.format_datetime(datetime.datetime.fromisoformat(TODAY+'T12:00:00+00:00'))
open(OUT+'/blog/feed.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom"><channel><title>FirearmSafety.us Blog</title><link>'+DOM+'/blog/</link><description>Firearm safety, California rules and training guides for beginners.</description><language>en-us</language><atom:link href="'+DOM+'/blog/feed.xml" rel="self" type="application/rss+xml"/>'+''.join(f'<item><title>{_h.escape(x[1])}</title><link>{DOM}/blog/{x[0]}/</link><guid>{DOM}/blog/{x[0]}/</guid><pubDate>{rfc}</pubDate><description>{_h.escape(x[2])}</description></item>' for x in POSTS)+'</channel></rss>\n')
bots=['Googlebot','Bingbot','GPTBot','OAI-SearchBot','ChatGPT-User','ClaudeBot','Claude-SearchBot','PerplexityBot','Google-Extended','Applebot','DuckDuckBot']
open(OUT+'/robots.txt','w').write('# FirearmSafety.us: search engines and AI answer engines welcome\n'+''.join(f'User-agent: {b}\nAllow: /\n\n' for b in bots)+f'User-agent: *\nAllow: /\nDisallow: /scripts/\n\nSitemap: {DOM}/sitemap.xml\n')
open(OUT+'/llms.txt','w').write('# FirearmSafety.us\n\n> Beginner guide to firearm safety and self-defense training in Southern California. Education only; no sales.\n\n'+''.join(f'- [{t}]({DOM}{p})\n' for p,(t,_,_) in list(P.items()))+''.join(f'- [{x[1]}]({DOM}/blog/{x[0]}/)\n' for x in POSTS))
open(OUT+'/README.md','w').write('# firearmsafety.us\n\nStatic GitHub Pages site. Regenerate pages with the build script, or edit the HTML directly. Partner: United Defense Tactical (Awin 128023).\n')
print('built',len(paths)+1,'pages')
