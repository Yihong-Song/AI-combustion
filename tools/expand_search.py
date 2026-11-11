import concurrent.futures

from discover import crossref


if __name__ == "__main__":
    jobs = [(query, issn, 100) for issn in ["0010-2180", "1540-7489", "0360-1285", "0016-2361"] for query in ["machine learning", "neural network", "deep learning", "physics informed"]]
    jobs += [(query, None, 100) for query in ["combustion machine learning", "combustion neural network", "flame neural network", "thermoacoustic machine learning", "combustion reinforcement learning", "combustion neural operator", "combustion generative adversarial", "combustion Bayesian learning", "combustion tomography deep learning", "combustion chemical kinetics neural", "hydrogen ammonia combustion machine learning", "combustion transformer", "flame graph neural network", "combustion active learning", "ignition delay machine learning", "flame speed machine learning", "soot machine learning", "spray combustion neural network"]]
    def run(job):
        query, result = crossref(*job)
        return query, result.get("issn"), len(result["items"])
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(run, jobs):
            print(result, flush=True)
