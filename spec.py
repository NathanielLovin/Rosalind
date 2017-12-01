import rna

L = [4439.32126116, 4567.41622116, 4666.48463116, 4737.52174116, 4900.58507116, 5014.62800116, 5085.66511116, 5214.70770116, 5351.76661116, 5465.80954116, 5602.86845116, 5788.94776116, 5886.00052116, 5987.04820116, 6143.14931116, 6274.18980116, 6403.23239116, 6516.31645116, 6645.35904116, 6773.41762116, 6860.44965116, 6973.53371116, 7159.61302116, 7306.68143116, 7434.74001116, 7571.79892116, 7670.86733116, 7833.93066116, 7947.01472116, 8062.04166116, 8176.08459116, 8263.11662116, 8334.15373116, 8421.18576116, 8549.24434116, 8678.28693116, 8779.33461116, 8893.37754116, 8980.40957116, 9051.44668116, 9182.48717116, 9239.50863116, 9353.55156116, 9516.61489116, 9644.67347116, 9772.73205116, 9829.75351116, 9960.79400116, 10088.8889612, 10187.9573712, 10289.0050512, 10403.0479812, 10490.0800112, 10591.1276912, 10692.1753712, 10795.1845612, 10910.2115012, 11096.2908112, 11210.3337412, 11307.3865012, 11364.4079612, 11492.4665412, 11589.5193012, 11676.5513312, 11804.6462912, 11933.6888812, 12046.7729412, 12177.8134312, 12306.8560212, 12453.9244312, 12550.9771912, 12679.0357712, 12736.0572312, 12849.1412912, 12980.1817812, 13067.2138112, 13230.2771412, 13317.3091712, 13404.3412012, 13518.3841312, 13633.4110712, 13789.5121812, 13917.5707612, 14030.6548212, 14127.7075812, 14198.7446912, 14329.7851812, 14476.8535912, 14589.9376512, 14726.9965612, 14856.0391512, 14927.0762612, 14984.0977212, 15097.1817812, 15200.1909712, 15303.2001612, 15466.2634912, 15581.2904312]
s = ""
for i in range(len(L)-1):
	a = L[i]
	b = L[i+1]
	m = round(b-a,7)
	p = rna.proteinOfMass(m)
	s += p
print s