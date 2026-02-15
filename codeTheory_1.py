def get_prime_factors(n):
    factors = {}
    d = 2
    temp = n
    while d * d <= temp:
        if temp % d == 0:
            count = 0
            while temp % d == 0:
                count += 1
                temp //= d
            factors[d] = count
        d += 1
    if temp > 1:
        factors[temp] = 1
    return factors


def solve_primitive_element():
    print("-" * 50)
    print("VÉGES TEST PRIMITÍV ELEMÉNEK MEGHATÁROZÁSA")
    print("-" * 50)

    try:
        Q = int(input("Add meg a test rendjét (pl. 13): "))
    except ValueError:
        print("Hiba: Kérlek számot adj meg!")
        return

    h = Q - 1
    print(f"\n1. Lépés: h = |Q| - 1 meghatározása")
    print(f"   h = {Q} - 1 = {h}")

    # prime factorization
    factors = get_prime_factors(h)
    factors_str = " * ".join([f"{p}^{r}" for p, r in factors.items()])
    print(f"   h prímtényezős alakja: {factors_str}")

    alphas = []

    # cycle of prime factor
    for i, (p, r) in enumerate(factors.items(), 1):
        p_r = p**r
        exponent_f = h // p
        exponent_alpha = h // p_r

        print(f"\n{i+1}. Lépés: Vizsgálat a p{i} = {p} ágon (p^{r} = {p_r})")
        print(f"   Az ellenőrző polinom képlete: f{i}(x) = x^(h/p{i}) - 1")
        print(f"   Behelyettesítve: f{i}(x) = x^({h}/{p}) - 1 = x^{exponent_f} - 1")

        beta = 2
        while True:
            # calculate beta^exponent_f Q mod
            val = pow(beta, exponent_f, Q)
            res = (val - 1) % Q

            print(
                f"   - Próba beta = {beta}: {beta}^{exponent_f} - 1 ≡ {val} - 1 ≡ {res} (mod {Q})"
            )

            if res != 0:
                print(f"     => {res} ≠ 0, a {beta} megfelelő alap.")
                break
            else:
                print(f"     => {res} = 0, a {beta} nem jó, nézzük a következőt.")
                beta += 1

        # calculate alpha
        alpha_i = pow(beta, exponent_alpha, Q)
        print(
            f"   alfa{i} kiszámítása: beta{i}^(h / p{i}^r{i}) = {beta}^({h}/{p_r}) = {beta}^{exponent_alpha}"
        )
        print(f"   alfa{i} = {alpha_i} (mod {Q})")
        alphas.append(alpha_i)

    # final results
    print(f"\n{len(factors)+2}. Lépés: A primitív elem (alfa) meghatározása")

    final_alpha = 1
    for a in alphas:
        final_alpha *= a

    final_alpha_mod = final_alpha % Q

    alphas_mult_str = " x ".join(map(str, alphas))
    print(f"   alfa = " + alphas_mult_str + f" = {final_alpha}")
    print(f"   alfa ≡ {final_alpha_mod} (mod {Q})")

    print(f"\nEREDMÉNY: A Z{Q} test egy primitív eleme: {final_alpha_mod}")

    # generate verification
    print("-" * 50)
    check = input("\nSzeretnéd látni az ellenőrzést (összes hatvány)? (i/n): ")
    if check.lower() == "i":
        print(f"\nEllenőrzés: Az {final_alpha_mod} hatványai Z{Q}-ban:")
        seen = []
        for e in range(1, Q):
            res = pow(final_alpha_mod, e, Q)
            print(f"   {final_alpha_mod}^{e:2} ≡ {res:2} (mod {Q})")
            seen.append(res)

        if len(set(seen)) == Q - 1:
            print(
                "\nSIKER: Az elem valóban generálja a test összes nullától különböző elemét!"
            )
        else:
            print("\nHIBA: az elem nem primitív.")


if __name__ == "__main__":
    solve_primitive_element()
