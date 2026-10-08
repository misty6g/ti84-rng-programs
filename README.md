# TI-84 Random Number Generator Programs

TI-BASIC programs for TI-84 Plus / Plus CE. Sources are in `src/`, ready-to-send files in `bin/`.

Send `bin/*.8xp` to the calculator with TI Connect CE, or type in the `src/*.txt` code by hand.
Rebuild after editing: `pip install tivars && python3 build.py`.

**`MATH301` combines all six into one program with a menu.** Send just `bin/MATH301.8xp` if you only want one program. After each tool finishes, press ENTER to return to the menu.

| Program | Inputs | Output |
|---|---|---|
| `LCG` | M, A, C, X0, COUNT (≤999) | X1..Xn on screen, saved to `L1` and `ʟLCG` |
| `HULLDOB` | M, A, C | Prime factors of M, each Hull–Dobell condition TRUE/FALSE, full-period verdict |
| `CARMICHL` | M (auto-factored) or prime/exponent lists | `{P,K,λ(P^K)}` per prime power (saved to `ʟLAM`) and λ(M) = LCM |
| `MODINV` | A, M | A⁻¹ mod M with check, or `NO INVERSE` and the gcd |
| `KSUNIF` | A list, e.g. `L1` | Sorted data (saved in `ʟKSR`), D+, D−, D (columns in `ʟDP`, `ʟDM`) |
| `LFSR` | Taps or polynomial, seed bits | Period length, then the first N bits (saved to `ʟLFSR`) |

## LFSR conventions

- **Taps mode:** `B(N) = B(N-T1) XOR B(N-T2) XOR ...`. Example: taps `{3,4}`.
- **Polynomial mode:** enter exponents, e.g. `x^4+x+1` → `{4,1,0}`. This is converted to taps `{3,4}`.
- **Seed:** `{B1,...,BK}` (oldest first), K = largest tap / degree. Example: `{1,0,0,0}`.
- The bit list starts with the seed, followed by the generated bits.
- Finding the period takes about 2^K steps, so K ≤ ~14 finishes quickly. Press ON to abort.

## Notes

- Arithmetic is exact while products stay below about 10^14. `LCG` warns when A·M is larger than that.
