import os,json,datetime
import pathlib; OUT=str(pathlib.Path(__file__).resolve().parent.parent)
DOM='https://firearmsafety.us'
UDT='https://www.awin1.com/cread.php?awinmid=128023&amp;awinaffid=3067297'
TODAY='2026-10-20'
BANNERS=['4893624','4893620','4893619','4893622']
def banner(i):
    b=BANNERS[i%len(BANNERS)]
    return f'<a class="bnr" rel="sponsored nofollow noopener" target="_blank" href="https://www.awin1.com/cread.php?s={b}&amp;v=128023&amp;q=615217&amp;r=3067297"><img src="https://www.awin1.com/cshow.php?s={b}&amp;v=128023&amp;q=615217&amp;r=3067297" alt="United Defense Tactical firearm training classes" loading="lazy" decoding="async"></a>'
CSS=r"""
:root{--paper:#F2F4F5;--ink:#18232B;--steel:#566672;--line:#D3D9DD;--orange:#E35D1B;--orange-ink:#B8440C;--white:#FFFFFF}
@media (prefers-color-scheme:dark){:root{--paper:#121A20;--ink:#E7ECEF;--steel:#9AA8B2;--line:#2A3640;--orange:#F07A3A;--orange-ink:#F49563;--white:#18232B}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--paper);color:var(--ink);font:400 1.125rem/1.7 "Source Serif 4",Georgia,serif}
a{color:inherit;text-decoration-color:var(--orange);text-underline-offset:3px;text-decoration-thickness:2px}
a:hover{color:var(--orange-ink)}
:focus-visible{outline:3px solid var(--orange);outline-offset:3px}
h1,h2,h3,.brand,.nav a,.btn,.rule-n{font-family:"Archivo",system-ui,sans-serif;font-stretch:112%}
h1{font-weight:800;font-size:clamp(2.2rem,6vw,3.6rem);line-height:1.05;letter-spacing:-.01em;margin:0 0 .5em}
h2{font-weight:750;font-size:clamp(1.45rem,3.2vw,1.9rem);line-height:1.15;margin:2.2em 0 .5em}
h3{font-weight:700;font-size:1.15rem;margin:1.6em 0 .3em}
p,li{max-width:68ch}
.wrap{max-width:1080px;margin:0 auto;padding:0 20px}
header.top{border-bottom:1px solid var(--line);background:var(--paper)}
header.top .wrap{display:flex;align-items:center;justify-content:space-between;gap:16px;padding-top:14px;padding-bottom:14px;flex-wrap:wrap}
.brand{font-weight:800;font-size:1.2rem;text-decoration:none;display:flex;align-items:center;gap:10px}
.brand i{display:inline-block;width:14px;height:14px;background:var(--orange);border-radius:3px}
.nav{display:flex;gap:18px;flex-wrap:wrap}
.nav a{font-size:.95rem;font-weight:600;text-decoration:none;color:var(--steel)}
.nav a[aria-current]{color:var(--ink);text-decoration:underline;text-decoration-color:var(--orange)}
main{padding:48px 0 72px}
.lede{font-size:1.3rem;line-height:1.55;color:var(--steel);max-width:58ch}
.hero{display:grid;grid-template-columns:1.05fr 1fr;gap:48px;align-items:start}
.rules{list-style:none;margin:0;padding:0;border-top:4px solid var(--orange)}
.rules li{display:grid;grid-template-columns:3.2rem 1fr;gap:12px;padding:16px 0;border-bottom:1px solid var(--line);max-width:none}
.rules .rule-n{font-weight:800;font-size:2.4rem;line-height:1;color:var(--orange)}
.rules b{display:block;font-family:"Archivo",system-ui,sans-serif;font-stretch:112%;font-size:1.15rem;line-height:1.25;margin-bottom:4px}
.rules div span{color:var(--steel);font-size:1rem;line-height:1.5}
.rules-cap{font-size:.9rem;color:var(--steel);margin-top:10px}
.btn{display:inline-block;font-weight:700;font-size:1rem;padding:13px 20px;border-radius:6px;text-decoration:none;background:var(--ink);color:var(--paper);margin:8px 10px 0 0}
.btn:hover{color:var(--paper);background:var(--orange-ink)}
.btn.alt{background:transparent;color:var(--ink);border:2px solid var(--ink)}
.btn.alt:hover{border-color:var(--orange-ink);color:var(--orange-ink);background:transparent}
.guides{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:0;border-top:1px solid var(--line);margin-top:20px}
.guides a{display:block;padding:20px 20px 20px 0;border-bottom:1px solid var(--line);text-decoration:none}
.guides a b{display:block;font-family:"Archivo",system-ui,sans-serif;font-stretch:112%;font-size:1.1rem}
.guides a span{color:var(--steel);font-size:1rem;line-height:1.5}
.guides a:hover b{color:var(--orange-ink)}
.partner{margin-top:56px;padding:28px;border:2px solid var(--ink);border-radius:8px;background:var(--white)}
.partner h2{margin-top:0}
.small{font-size:.9rem;color:var(--steel)}
.bnr{display:block;margin:20px 0 4px;max-width:100%}.bnr img{display:block;max-width:100%;height:auto;border-radius:6px}
.article{max-width:720px}
.article ul,.article ol{padding-left:1.3em}
.article li{margin:.35em 0}
.note{border-left:4px solid var(--orange);padding:4px 0 4px 16px;margin:24px 0;color:var(--steel)}
.check li::marker{color:var(--orange)}
footer{border-top:1px solid var(--line);padding:28px 0 40px;font-size:.95rem;color:var(--steel)}
footer .wrap{display:flex;justify-content:space-between;gap:20px;flex-wrap:wrap}
footer nav{display:flex;gap:16px;flex-wrap:wrap}
@media (max-width:820px){.hero{grid-template-columns:1fr;gap:28px}main{padding-top:32px}}
"""
NAV=[('/choose-a-class/','Choose a class'),('/first-class/','Your first class'),('/safety-storage/','Safety & storage'),('/self-defense-basics/','Self-defense basics'),('/la-orange-county/','LA & Orange County'),('/blog/','Blog')]
FOOT=[('/about/','About'),('/affiliate-disclosure/','Affiliate disclosure'),('/privacy/','Privacy'),('/terms/','Terms')]
def page(path,title,desc,body,schema=None):
    cur=lambda h:' aria-current="page"' if h==path else ''
    nav=''.join(f'<a href="{h}"{cur(h)}>{t}</a>' for h,t in NAV)
    foot=''.join(f'<a href="{h}">{t}</a>' for h,t in FOOT)
    url=DOM+path
    sch=f'<script type="application/ld+json">{json.dumps(schema)}</script>' if schema else ''
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{url}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:type" content="website"><meta name="twitter:card" content="summary_large_image"><meta property="og:image" content="{DOM}/og-image.jpg">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><meta name="theme-color" content="#18232B">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@100..125,600..800&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css">{sch}</head><body>
<header class="top"><div class="wrap"><a class="brand" href="/"><i aria-hidden="true"></i>FirearmSafety.us</a><nav class="nav" aria-label="Main">{nav}</nav></div></header>
<main id="main"><div class="wrap">{body}</div></main>
<footer><div class="wrap"><p>FirearmSafety.us is an independent safety-education guide. It does not sell firearms, ammunition or accessories.</p><nav aria-label="Footer">{foot}</nav></div></footer>
</body></html>'''
def write(path,html):
    d=OUT+path; os.makedirs(d,exist_ok=True); global _bi
    _bi=globals().get('_bi',-1)+1
    open(d+'index.html','w').write(html.replace('{UDT}',UDT).replace('{BANNER}',banner(_bi)))
PARTNER=f'''<section class="partner" aria-labelledby="p-title"><h2 id="p-title">Find a class with United Defense Tactical</h2>
<p>United Defense Tactical teaches firearms safety, shooting fundamentals and self-defense classes in Southern California, with instructors working in Los Angeles and Orange County.</p>
<a class="btn" href="{UDT}" target="_blank" rel="sponsored nofollow noopener">See classes and dates</a>{{BANNER}}
<p class="small">Sponsored link. If you book through it, we may earn a commission at no extra cost to you. <a href="/affiliate-disclosure/">How we work with partners</a></p></section>'''
ART=lambda h1,lede,inner: f'<article class="article"><h1>{h1}</h1><p class="lede">{lede}</p>{inner}</article>'+PARTNER
def artschema(t,d,p): return {"@context":"https://schema.org","@type":"Article","headline":t,"description":d,"mainEntityOfPage":DOM+p,"datePublished":TODAY,"dateModified":TODAY,"author":{"@type":"Organization","name":"FirearmSafety.us"},"publisher":{"@type":"Organization","name":"FirearmSafety.us","url":DOM}}

# Home
rules=[('Treat every firearm as if it is loaded.','Even when someone has just shown you it is empty. Check it yourself, every time.'),
('Never point the muzzle at anything you are not willing to destroy.','Keep it pointed in a safe direction while you hold it, hand it over or put it down.'),
('Keep your finger off the trigger until your sights are on target and you have decided to shoot.','Rest it straight along the frame instead.'),
('Be sure of your target and what is beyond it.','A shot can pass through or miss. Know where it will stop.')]
rl=''.join(f'<li><span class="rule-n" aria-hidden="true">{i+1}</span><div><b>{a}</b><span>{b}</span></div></li>' for i,(a,b) in enumerate(rules))
guides=[('/choose-a-class/','Choose a class','What to compare between instructors, class types and ranges.'),
('/first-class/','Your first class','What happens on the day, what to bring and what to wear.'),
('/safety-storage/','Safety &amp; storage','Locking, storing and transporting firearms at home and in the car.'),
('/self-defense-basics/','Self-defense basics','Awareness, avoidance and de-escalation come before any tool.'),
('/la-orange-county/','LA &amp; Orange County','Training in Southern California and the state rules to know first.')]
gl=''.join(f'<a href="{h}"><b>{t}</b><span>{d}</span></a>' for h,t,d in guides)
home=f'''<section class="hero"><div><h1>Learn to handle a firearm safely, from your first class on.</h1>
<p class="lede">A plain-language guide for adults who are new to firearms or self-defense training in Southern California: how to choose a class, what to expect, and how to stay safe at home.</p>
<a class="btn" href="/choose-a-class/">Start with choosing a class</a><a class="btn alt" href="/first-class/">What your first class is like</a></div>
<div><ol class="rules" aria-label="The four rules of firearm safety">{rl}</ol><p class="rules-cap">Every good class starts with these four rules. Learn them before you touch a firearm.</p></div></section>
<h2>Guides</h2><div class="guides">{gl}</div>{PARTNER}'''
write('/', page('/','FirearmSafety.us: firearm safety and self-defense training for beginners','A beginner guide to firearm safety and self-defense training in Southern California: choosing a class, your first lesson, safe storage and state rules.',home,
 {"@context":"https://schema.org","@type":"WebSite","name":"FirearmSafety.us","url":DOM}))

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
<p class="note">Requirements to buy or own a firearm vary by state. In California, check the current rules with the <a href="https://oag.ca.gov/firearms" rel="noopener" target="_blank">California Department of Justice</a>.</p>'''))
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
<h2>If you feel nervous</h2><p>That is normal and useful: it keeps you careful. Tell the instructor at the start. You can always pause, ask questions, or skip the live-fire part and come back another day.</p>'''))
P['/safety-storage/']=('Safe firearm storage and transport at home','How to lock, store and transport firearms safely, especially in homes with children or visitors.',
 ART('Safe storage and transport','Most firearm accidents at home happen when someone who should not have access finds an unsecured gun. Storage is part of safety, not an extra.',
 '''<h2>Storage at home</h2><ul class="check">
<li><b>Lock it up.</b> Use a gun safe, lockbox or locking device. A locked container is the safest option.</li>
<li><b>Store ammunition separately</b> when you can, also locked.</li>
<li><b>Control the keys and codes.</b> Do not hide keys where children or visitors can find them.</li>
<li><b>Unload before storing</b>, unless you have a specific, well-considered reason and secure storage.</li></ul>
<h2>Children and visitors</h2><p>Children are curious and can find hiding places adults think are secret. Teach them that if they ever see a gun, they should not touch it, leave the area and tell an adult. When visitors stay over, check that everything is locked away.</p>
<h2>Transport</h2><p>Carry firearms unloaded and in a locked container, and follow your state's transport rules. Rules differ between states and can change, so check before you travel.</p>
<p class="note">California has specific storage and transport laws. Read the current requirements on the <a href="https://oag.ca.gov/firearms" rel="noopener" target="_blank">California Department of Justice firearms pages</a>.</p>'''))
P['/self-defense-basics/']=('Self-defense basics: awareness, avoidance and de-escalation','The foundations of personal safety that come before any self-defense tool: awareness, avoidance, de-escalation and knowing the law.',
 ART('Self-defense basics','Good self-defense training spends most of its time on not needing to defend yourself at all.',
 '''<h2>Awareness</h2><p>Notice your surroundings: exits, who is nearby, what feels out of place. Put the phone away in parking lots and at transit stops, and trust the feeling that something is wrong.</p>
<h2>Avoidance</h2><p>The best outcome is not being there. Change direction, cross the street, go into a busy shop, or leave early. Plan routes and travel with others when you can.</p>
<h2>De-escalation</h2><p>Keep distance, keep your hands visible, speak calmly and give the other person a way out. Property can be replaced. Walking away is a win.</p>
<h2>Know the law</h2><p>Self-defense law is specific and varies by state. A good course explains when force is and is not lawful. For advice about your situation, talk to a qualified attorney.</p>
<h2>Where firearm training fits</h2><p>If you choose to own a firearm for home defense, safety and regular practice with a qualified instructor matter more than the equipment. Start with a <a href="{UDT}" target="_blank" rel="sponsored nofollow noopener">beginner safety class</a>.</p>'''))
P['/la-orange-county/']=('Firearm safety training in Los Angeles and Orange County','Training options in Southern California and the California rules beginners should know before buying or carrying a firearm.',
 ART('Training in Los Angeles and Orange County','Southern California has indoor and outdoor ranges and many private instructors. California also has some of the most detailed firearm rules in the US, so start with the basics.',
 '''<h2>Rules to know first in California</h2><ul class="check">
<li><b>Firearm Safety Certificate (FSC):</b> generally required before you can buy a firearm in California. The test covers basic safety and law.</li>
<li><b>Waiting period:</b> California requires a waiting period before a purchased firearm can be picked up.</li>
<li><b>Carry permits:</b> carrying a concealed firearm needs a county-issued license, which includes required training.</li></ul>
<p class="note">Rules change. Always confirm the current requirements with the <a href="https://oag.ca.gov/firearms" rel="noopener" target="_blank">California Department of Justice</a> and your county sheriff or police department.</p>
<h2>Choosing where to train</h2><p>Look for classes close enough that you will go back for practice. Ask about class size, whether rentals and protective gear are available, and whether the instructor offers a follow-up session.</p>
<h2>Next steps</h2><p>Read <a href="/choose-a-class/">how to choose a class</a> and <a href="/first-class/">what your first class is like</a>, then <a href="{UDT}" target="_blank" rel="sponsored nofollow noopener">book a beginner session</a>.</p>'''))
for p,(t,d,b) in P.items(): write(p,page(p,t+' | FirearmSafety.us',d,b,artschema(t,d,p)))

legal={
'/about/':('About FirearmSafety.us','Who runs FirearmSafety.us and how we write our guides.','<article class="article"><h1>About FirearmSafety.us</h1><p class="lede">FirearmSafety.us is an independent guide for adults who are new to firearm safety and self-defense training.</p><p>We focus on safety, choosing qualified instructors and following the law. We do not sell firearms, ammunition or accessories, and we do not publish tactical instruction. For legal requirements we link to official sources instead of interpreting them.</p><p>FirearmSafety.us is published by GetServices.ai. Questions or corrections: <a href="mailto:hello@getservices.ai">hello@getservices.ai</a>.</p></article>'),
'/affiliate-disclosure/':('Affiliate disclosure','How FirearmSafety.us works with partners and earns commission.','<article class="article"><h1>Affiliate disclosure</h1><p class="lede">Some links on this site are affiliate links. If you book a class through them, we may earn a commission at no extra cost to you.</p><p>Our current partner is United Defense Tactical, through the Awin affiliate network. Partner links are marked as sponsored. Commission never changes our safety advice.</p></article>'),
'/privacy/':('Privacy policy','How FirearmSafety.us handles your data.','<article class="article"><h1>Privacy policy</h1><p class="lede">We collect as little as possible.</p><p>This site has no accounts or forms. It loads fonts from Google Fonts, which receives your IP address when the fonts load. When you click a partner link, the Awin network and the partner may set cookies to track the referral. See their privacy policies for details. Contact: <a href="mailto:hello@getservices.ai">hello@getservices.ai</a>.</p></article>'),
'/terms/':('Terms of use','Terms for using FirearmSafety.us.','<article class="article"><h1>Terms of use</h1><p class="lede">FirearmSafety.us is for general education only.</p><p>It is not legal advice and is not a substitute for in-person instruction from a qualified instructor. Laws vary and change, so check current requirements with official sources. You are responsible for following the law and range rules. Content may change without notice.</p></article>'),
}
write('/blog/', page('/blog/','Blog | FirearmSafety.us','Guides and articles on firearm safety and training for beginners.','<h1>Blog</h1><p class="lede">New guides on firearm safety and training are published here. Start with <a href="/choose-a-class/">choosing a class</a> or <a href="/first-class/">what your first class is like</a>.</p>'))
for p,(t,d,b) in legal.items(): write(p,page(p,t+' | FirearmSafety.us',d,b))
open(OUT+'/404.html','w').write(page('/404/','Page not found | FirearmSafety.us','This page does not exist.','<h1>This page does not exist.</h1><p class="lede">It may have moved. Go to the <a href="/">home page</a> or start with <a href="/choose-a-class/">choosing a class</a>.</p>'))
open(OUT+'/styles.css','w').write(CSS.strip())
open(OUT+'/CNAME','w').write('firearmsafety.us\n')
open(OUT+'/favicon.svg','w').write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="6" fill="#18232B"/><rect x="9" y="9" width="14" height="14" rx="3" fill="#E35D1B"/></svg>')
paths=['/']+list(P)+['/blog/']+list(legal)
open(OUT+'/sitemap.xml','w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{DOM}{p}</loc><lastmod>{TODAY}</lastmod></url>' for p in paths)+'</urlset>\n')
open(OUT+'/robots.txt','w').write(f'User-agent: *\nAllow: /\nSitemap: {DOM}/sitemap.xml\n')
open(OUT+'/llms.txt','w').write('# FirearmSafety.us\n\n> Beginner guide to firearm safety and self-defense training in Southern California. Education only; no sales.\n\n'+''.join(f'- [{t}]({DOM}{p})\n' for p,(t,_,_) in list(P.items())))
open(OUT+'/README.md','w').write('# firearmsafety.us\n\nStatic GitHub Pages site. Regenerate pages with the build script, or edit the HTML directly. Partner: United Defense Tactical (Awin 128023).\n')
print('built',len(paths)+1,'pages')
