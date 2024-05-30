import numpy as np
import scipy.stats as st


def analytical_ci_z(data, confidence=0.95):
    mean = np.mean(data)
    sem = st.sem(data)
    z = st.norm.ppf((1 + confidence) / 2)
    h = sem * z
    return mean - h, mean + h


def clean_string(s):
    if isinstance(s, str):
        return s.lower().strip()
    return s


def bootstrap(data, num_samples=10000, ci=95):
    samples = np.random.choice(data, (num_samples, len(data)), replace=True)
    means = np.mean(samples, axis=1)
    lower_bound = np.percentile(means, (100-ci)/2)
    upper_bound = np.percentile(means, 100-(100-ci)/2)
    return lower_bound, upper_bound
