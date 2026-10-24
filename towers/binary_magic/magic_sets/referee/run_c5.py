import sys, json
sys.path.insert(0, __import__('os').path.dirname(__import__('os').path.abspath(__file__)))
from canon_search import search, to_str
sets = json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), '..', 'graph_star_sets.json')))
ctx = sets['C5 (n=5)']['contexts']
for k in [int(a) for a in sys.argv[1:]]:
    st, fd, obs = search(ctx, k, time_limit=3000)
    print('C5 k=%d' % k, st, flush=True)
    for f in fd[:1]:
        print('  magic example:', dict(zip(obs, [to_str(v, k) for v in f])), flush=True)
