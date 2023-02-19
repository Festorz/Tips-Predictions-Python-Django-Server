# field user
def PREMIUM(modelAdmin, request, queryset):
    queryset.update(premium=True)


def VIP(modelAdmin, request, queryset):
    queryset.update(VIP=True)


def FIXEDMATCHES(modelAdmin, request, queryset):
    queryset.update(fixedMatches=True)


def GURUTIPS(modelAdmin, request, queryset):
    queryset.update(guruTips=True)


def Jackpot(modelAdmin, request, queryset):
    queryset.update(jackpot=True)


def not_PREMIUM(modelAdmin, request, queryset):
    queryset.update(premium=False)


def not_VIP(modelAdmin, request, queryset):
    queryset.update(VIP=False)


def not_FIXEDMATCHES(modelAdmin, request, queryset):
    queryset.update(fixedMatches=False)


def not_GURUTIPS(modelAdmin, request, queryset):
    queryset.update(guruTips=False)


def not_Jackpot(modelAdmin, request, queryset):
    queryset.update(jackpot=False)


def DEFAULT(modelAdmin, request, queryset):
    queryset.update(jackpot=False, premium=False, VIP=False,
                    fixedMatches=False, guruTips=False)

# field mutlibets


def Btts(modelAdmin, request, queryset):
    queryset.update(btts=True)


def Over_Under(modelAdmin, request, queryset):
    queryset.update(ov_und=True)


def ix2(modelAdmin, request, queryset):
    queryset.update(iX2=True)


def Htft(modelAdmin, request, queryset):
    queryset.update(ht_ft=True)


def NULL(modelAdmin, request, queryset):
    queryset.update(booked='', ht_ft=False, btts=False,
                    ov_und=False, iX2=False)

# field jackpots subscribers


def sport_mega(modelAdmin, request, queryset):
    queryset.update(sport_mega=True)


def betika(modelAdmin, request, queryset):
    queryset.update(betika=True)


def betpawa(modelAdmin, request, queryset):
    queryset.update(betpawa=True)


def bet9ja(modelAdmin, request, queryset):
    queryset.update(bet9ja=True)


def null_jackpot(modelAdmin, request, queryset):
    queryset.update(booked='', sport_mega=False, betika=False,
                    betpawa=False, bet9ja=False)
