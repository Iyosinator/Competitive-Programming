use std::io::{self, BufRead};

fn main() {
    let stdin = io::stdin();
    let mut lines = stdin.lock().lines();

    let n: usize = lines.next().unwrap().unwrap().trim().parse().unwrap();
    let mut a = vec![0; n];
    for i in 0..n {
        let line = lines.next().unwrap().unwrap();
        let mut parts = line.split_whitespace();
        let x: usize = parts.next().unwrap().parse().unwrap();
        let y: usize = parts.next().unwrap().parse().unwrap();
        a[x - 1] = y - 1;
    }

    let mut lmax = vec![0; n];
    let mut rmax = vec![0; n];
    let mut lmin = vec![0; n];
    let mut rmin = vec![0; n];
    let mut cnt = vec![0i64; 2 * n];

    fn solve(
        l: usize,
        r: usize,
        a: &Vec<usize>,
        lmax: &mut Vec<usize>,
        rmax: &mut Vec<usize>,
        lmin: &mut Vec<usize>,
        rmin: &mut Vec<usize>,
        cnt: &mut Vec<i64>,
        n: usize,
    ) -> i64 {
        if r - l == 1 {
            return 1;
        }
        let m = (l + r) / 2;
        let mut result = solve(l, m, a, lmax, rmax, lmin, rmin, cnt, n) + solve(m, r, a, lmax, rmax, lmin, rmin, cnt, n);

        lmin[m - 1] = a[m - 1];
        lmax[m - 1] = a[m - 1];
        for i in (l..m - 1).rev() {
            lmin[i] = lmin[i + 1].min(a[i]);
            lmax[i] = lmax[i + 1].max(a[i]);
        }

        rmin[m] = a[m];
        rmax[m] = a[m];
        for i in m + 1..r {
            rmin[i] = rmin[i - 1].min(a[i]);
            rmax[i] = rmax[i - 1].max(a[i]);
        }

        for x in l..m {
            let y = x + lmax[x] - lmin[x];
            if y >= m && y < r && rmax[y] < lmax[x] && rmin[y] > lmin[x] {
                result += 1;
            }
        }

        for y in m..r {
            let x = y - rmax[y] + rmin[y];
            if x >= l && x < m && lmax[x] < rmax[y] && lmin[x] > rmin[y] {
                result += 1;
            }
        }

        // First counting loop
        let mut s = m;
        let mut t = m;
        while s < cnt.len() { cnt[s] = 0; s += 1; } // reset cnt for safety
        s = m;
        t = m;

        for x in (l..m).rev() {
            while t < r && rmin[t] > lmin[x] {
                cnt[t - rmax[t] + n] += 1;
                t += 1;
            }
            while s < t && rmax[s] < lmax[x] {
                cnt[s - rmax[s] + n] -= 1;
                s += 1;
            }
            result += cnt[x - lmin[x] + n];
        }

        while s < t {
            cnt[s - rmax[s] + n] -= 1;
            s += 1;
        }

        // Second counting loop
        s = m;
        t = m;
        while s < cnt.len() { cnt[s] = 0; s += 1; }
        s = m;
        t = m;

        for x in (l..m).rev() {
            while t < r && rmax[t] < lmax[x] {
                cnt[t + rmin[t]] += 1;
                t += 1;
            }
            while s < t && rmin[s] > lmin[x] {
                cnt[s + rmin[s]] -= 1;
                s += 1;
            }
            result += cnt[x + lmax[x]];
        }

        while s < t {
            cnt[s + rmin[s]] -= 1;
            s += 1;
        }

        result
    }

    let ans = solve(0, n, &a, &mut lmax, &mut rmax, &mut lmin, &mut rmin, &mut cnt, n);
    println!("{}", ans);
}
