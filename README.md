# MATH301 — TI-84 Random Number Generator Toolkit

A single menu-driven TI-BASIC program for TI-84 Plus / Plus CE. Source: `src/MATH301.txt`; ready-to-send file: `bin/MATH301.8xp`.

Send `bin/MATH301.8xp` to the calculator with TI Connect CE. Rebuild after editing: `pip install tivars && python3 build.py`.

Results are only displayed; nothing is saved. Scratch lists used while a tool runs are deleted when you return to the menu.

The main menu has two tabs, **RNG TOOLS** and **QUIZ 4**; each tool returns to its own tab.

### RNG TOOLS

| Menu item | Inputs | Output |
|---|---|---|
| LCG | M, A, C, X0, COUNT | X1..Xn |
| HULL-DOBELL | M, A, C | Prime factors of M, each Hull–Dobell condition TRUE/FALSE, full-period verdict |
| CARMICHAEL | M (auto-factored) or prime/exponent lists | `{P,K,λ(P^K)}` per prime power and λ(M) = LCM |
| MOD INVERSE | A, M | A⁻¹ mod M with check, or `NO INVERSE` and the gcd |
| KS UNIFORM | A list, e.g. `{.44,.81,.14}` or `L1` | Sorted data, D+, D−, D |
| LFSR | Taps or polynomial, seed bits | Period length, then the first N bits |

### QUIZ 4

| Menu item | Inputs | Output |
|---|---|---|
| GEN INVERSE | Outcome list, probability list, U | `{Xj,Pj,F(j)}` table, the interval F(j−1) ≤ U < F(j), and X |
| ACCEPT-REJECT | Outcome list, target Pj, reference Qj, optional c, then candidate Y and U | Ratios Pj/Qj, minimum c, 1/c, expected attempts c, then T = P_Y/(c·Q_Y) and ACCEPT (U < T) or REJECT; repeats for the next Y until accepted |
| POISSON INV | λ, U | `{i,Pi,F(i)}` table via P(i+1) = λ·P(i)/(i+1), stopping at the first U < F(i), then X |
| BINOMIAL INV | n, p, U | c = p/(1−p), `{i,Pi,F(i)}` table via P(i+1) = c·(n−i)/(i+1)·P(i), then X |
| ALIAS SETUP | Probability list for values 1..n, then your i, j at each step | Remaining PMF at each step (with a suggested i, j), the two-point Q for each step, the final mixture P = ΣQ(m)/(n−1), and a reconstruction check |

Table rows are rounded to 4 decimals for display, but every comparison uses full precision. In ACCEPT-REJECT, enter `0` for c to use the minimum c = max Pj/Qj, and enter a Y that isn't in the outcome list to exit. In ALIAS SETUP, a step is valid when Pi ≤ 1/(k−1) and Pi + Pj ≥ 1/(k−1), where k is the number of values remaining.

## LFSR conventions

- **Taps mode:** `B(N) = B(N-T1) XOR B(N-T2) XOR ...`. Example: taps `{3,4}`.
- **Polynomial mode:** enter exponents, e.g. `x^4+x+1` → `{4,1,0}`. This is converted to taps `{3,4}`.
- **Seed:** `{B1,...,BK}` (oldest first), K = largest tap / degree. Example: `{1,0,0,0}`.
- The bits shown start with the seed, followed by the generated bits.
- Finding the period takes about 2^K steps, so K ≤ ~14 finishes quickly. Press ON to abort.

## Notes

- Arithmetic is exact while products stay below about 10^14. LCG warns when A·M is larger than that.
