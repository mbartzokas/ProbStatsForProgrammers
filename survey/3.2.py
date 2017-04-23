def BiasPmf(pmf, runnersSpeed):
    biased = pmf.Copy()

    for speed, p in pmf.Items():
        differece = speed - runnersSpeed
        if differece < 0:
            biased.Mult(speed, 1.0 / abs(differece))
        else:
            biased.Mult(speed, abs(differece))

    biased.Normalize()

    return biased
