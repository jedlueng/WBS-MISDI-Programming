adjustments = []
for i in range(len(Sales)):
adjustment = Profit[i] – Sales[i] * rate
adjustments.append(adjustment) return adjustments


SCRIPT_REAL(
"
adjustments = []
for i in range(len(_arg1)):
adjustment = _arg2[i] - _arg1[i]*_arg3[0]
adjustments.append(adjustment) return adjustments
",
SUM([Sales]),
SUM([Profit]),
[rate]