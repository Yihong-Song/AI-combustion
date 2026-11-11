import concurrent.futures

from discover import crossref


if __name__ == "__main__":
    jobs = [(query, issn, 1000) for issn in ["0010-2180", "1540-7489", "0360-1285", "0016-2361"] for query in ["machine learning", "neural network", "physics informed"]]
    def run(job):
        try:
            query, result = crossref(*job)
            return query, result["issn"], len(result["items"])
        except Exception as error:
            return job, str(error)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        for result in pool.map(run, jobs):
            print(result, flush=True)
