import numpy as np

#MCW-RN

mcw_rn = []

mcw_rn.append([0.9822221994400024, 0.9826262, 0.9822221994400024, 0.9822221994400024])
mcw_rn.append([0.9777777791023254, 0.97722054, 0.9821428656578064, 0.9777777791023254])
mcw_rn.append([0.9777777791023254, 0.97722054, 0.9821428656578064, 0.9777777791023254])
mcw_rn.append([0.9599999785423279, 0.9590045, 0.9599999785423279, 0.9599999785423279])
mcw_rn.append([0.9822221994400024, 0.9817264, 0.9866071343421936, 0.9822221994400024])
mcw_rn.append([0.9822221994400024, 0.982226, 0.9821428656578064, 0.9777777791023254])
mcw_rn.append([0.9599999785423279, 0.9587661, 0.9856459498405457, 0.9155555367469788])
mcw_rn.append([0.9822221994400024, 0.98218703, 0.9866071343421936, 0.9822221994400024])
mcw_rn.append([0.9777777791023254, 0.9781638, 0.9821428656578064, 0.9777777791023254])
mcw_rn.append([0.9866666793823242, 0.98594856, 0.9865471124649048, 0.9777777791023254])
mcw_rn.append([0.9866666793823242, 0.98644686, 0.9866071343421936, 0.9822221994400024])
mcw_rn.append([0.9777777791023254, 0.97722054, 0.9777777791023254, 0.9777777791023254])
mcw_rn.append([0.9777777791023254, 0.97722054, 0.9777777791023254, 0.9777777791023254])
mcw_rn.append([0.9777777791023254, 0.97761977, 0.9821428656578064, 0.9777777791023254])
mcw_rn.append([0.9822221994400024, 0.9818404, 0.9821428656578064, 0.9777777791023254])
mcw_rn.append([0.9822221994400024, 0.9814414, 0.9821428656578064, 0.9777777791023254])
mcw_rn.append([0.9866666793823242, 0.98666024, 0.9866666793823242, 0.9866666793823242])
mcw_rn.append([0.9911110997200012, 0.990955, 0.9910314083099365, 0.9822221994400024])
mcw_rn.append([0.9822221994400024, 0.9817264, 0.9866071343421936, 0.9822221994400024])
mcw_rn.append([0.9866666793823242, 0.98594856, 0.9866666793823242, 0.9866666793823242])
mcw_rn.append([0.9822221994400024, 0.9814414, 0.9865471124649048, 0.9777777791023254])
mcw_rn.append([0.9822221994400024, 0.9817264, 0.9866071343421936, 0.9822221994400024])
mcw_rn.append([0.9822221994400024, 0.9814439, 0.9821428656578064, 0.9777777791023254])
mcw_rn.append([0.9822221994400024, 0.98214525, 0.9910314083099365, 0.9822221994400024])

mcw_rn_acc = []
mcw_rn_prec = []
mcw_rn_rec = []
mcw_rn_f1 = []
for solution in mcw_rn:
    mcw_rn_acc.append(solution[0])
    mcw_rn_prec.append(solution[1])
    mcw_rn_rec.append(solution[2])
    mcw_rn_f1.append(solution[3])

print("MCW-RN\n")
print(f"Best acc: {np.max(mcw_rn_acc)}, worst acc: {np.min(mcw_rn_acc)}, mean acc: {np.mean(mcw_rn_acc)}, std acc: {np.std(mcw_rn_acc)}")
print(f"Best prec: {np.max(mcw_rn_prec)}, worst prec: {np.min(mcw_rn_prec)}, mean prec: {np.mean(mcw_rn_prec)}, std prec: {np.std(mcw_rn_prec)}")
print(f"Best rec: {np.max(mcw_rn_rec)}, worst rec: {np.min(mcw_rn_rec)}, mean rec: {np.mean(mcw_rn_rec)}, std rec: {np.std(mcw_rn_rec)}")
print(f"Best f1: {np.max(mcw_rn_f1)}, worst f1: {np.min(mcw_rn_f1)}, mean f1: {np.mean(mcw_rn_f1)}, std f1: {np.std(mcw_rn_f1)}\n\n")

#MCW-XC

mcw_xc = []

mcw_xc.append([0.9822221994400024, 0.9817264, 0.9822221994400024, 0.9822221994400024])
mcw_xc.append([0.9822221994400024, 0.9816864, 0.9822221994400024, 0.9822221994400024])
mcw_xc.append([0.9866666793823242, 0.98673284, 0.9866666793823242, 0.9866666793823242])
mcw_xc.append([0.9777777791023254, 0.9780404, 0.9777777791023254, 0.9777777791023254])
mcw_xc.append([0.9733333587646484, 0.9726704, 0.9732142686843872, 0.9688888788223267])
mcw_xc.append([0.9822221994400024, 0.9826262, 0.9822221994400024, 0.9822221994400024])
mcw_xc.append([0.9822221994400024, 0.9817264, 0.9865471124649048, 0.9777777791023254])
mcw_xc.append([0.9822221994400024, 0.98214525, 0.9819004535675049, 0.9644444584846497])
mcw_xc.append([0.9644444584846497, 0.96345896, 0.9684684872627258, 0.9555555582046509])
mcw_xc.append([0.9822221994400024, 0.98214525, 0.9822221994400024, 0.9822221994400024])
mcw_xc.append([0.9866666793823242, 0.98594856, 0.9864864945411682, 0.9733333587646484])
mcw_xc.append([0.9822221994400024, 0.9817264, 0.9822221994400024, 0.9822221994400024])
mcw_xc.append([0.9777777791023254, 0.976373, 0.9820627570152283, 0.9733333587646484])
mcw_xc.append([0.9822221994400024, 0.9814439, 0.9865471124649048, 0.9777777791023254])
mcw_xc.append([0.9866666793823242, 0.9862419, 0.9910314083099365, 0.9822221994400024])
mcw_xc.append([0.9777777791023254, 0.97761977, 0.9777777791023254, 0.9777777791023254])
mcw_xc.append([0.9777777791023254, 0.97761977, 0.9777777791023254, 0.9777777791023254])
mcw_xc.append([0.9777777791023254, 0.97722054, 0.9777777791023254, 0.9777777791023254])
mcw_xc.append([0.9822221994400024, 0.98214525, 0.9820627570152283, 0.9733333587646484])
mcw_xc.append([0.9777777791023254, 0.97761977, 0.9820627570152283, 0.9733333587646484])
mcw_xc.append([0.9777777791023254, 0.9769149, 0.9821428656578064, 0.9777777791023254])
mcw_xc.append([0.9822221994400024, 0.9826262, 0.9822221994400024, 0.9822221994400024])
mcw_xc.append([0.9644444584846497, 0.9638678, 0.9686098694801331, 0.9599999785423279])
mcw_xc.append([0.9733333587646484, 0.97306836, 0.9733333587646484, 0.9733333587646484])

mcw_xc_acc = []
mcw_xc_prec = []
mcw_xc_rec = []
mcw_xc_f1 = []
for solution in mcw_xc:
    mcw_xc_acc.append(solution[0])
    mcw_xc_prec.append(solution[1])
    mcw_xc_rec.append(solution[2])
    mcw_xc_f1.append(solution[3])

print("MCW-XC\n")
print(f"Best acc: {np.max(mcw_xc_acc)}, worst acc: {np.min(mcw_xc_acc)}, mean acc: {np.mean(mcw_xc_acc)}, std acc: {np.std(mcw_xc_acc)}")
print(f"Best prec: {np.max(mcw_xc_prec)}, worst prec: {np.min(mcw_xc_prec)}, mean prec: {np.mean(mcw_xc_prec)}, std prec: {np.std(mcw_xc_prec)}")
print(f"Best rec: {np.max(mcw_xc_rec)}, worst rec: {np.min(mcw_xc_rec)}, mean rec: {np.mean(mcw_xc_rec)}, std rec: {np.std(mcw_xc_rec)}")
print(f"Best f1: {np.max(mcw_xc_f1)}, worst f1: {np.min(mcw_xc_f1)}, mean f1: {np.mean(mcw_xc_f1)}, std f1: {np.std(mcw_xc_f1)}\n\n")

#PI-RN

pi_rn = []

pi_rn.append([0.9976744055747986, 0.9976233, 0.9976744055747986, 0.9976744055747986])
pi_rn.append([0.9976744055747986, 0.9976233, 0.9976744055747986, 0.9976744055747986])
pi_rn.append([1.0, 1.0, 1.0, 1.0])
pi_rn.append([1.0, 1.0, 1.0, 1.0])
pi_rn.append([1.0, 1.0, 1.0, 1.0])
pi_rn.append([0.9976744055747986, 0.9976233, 0.9976744055747986, 0.9976744055747986])
pi_rn.append([0.9976744055747986, 0.9976233, 0.9976744055747986, 0.9976744055747986])
pi_rn.append([1.0, 1.0, 1.0, 1.0])
pi_rn.append([1.0, 1.0, 1.0, 1.0])
pi_rn.append([0.9976744055747986, 0.9976233, 0.9976744055747986, 0.9976744055747986])
pi_rn.append([0.9976744055747986, 0.9976233, 0.9976744055747986, 0.9976744055747986])
pi_rn.append([1.0, 1.0, 1.0, 1.0])
pi_rn.append([0.9953488111495972, 0.99525005, 0.9953488111495972, 0.9953488111495972])
pi_rn.append([1.0, 1.0, 1.0, 1.0])
pi_rn.append([1.0, 1.0, 1.0, 1.0])
pi_rn.append([0.9953488111495972, 0.99525005, 0.9953488111495972, 0.9953488111495972])
pi_rn.append([0.9976744055747986, 0.9976233, 0.9976744055747986, 0.9976744055747986])
pi_rn.append([1.0, 1.0, 1.0, 1.0])
pi_rn.append([1.0, 1.0, 1.0, 1.0])
pi_rn.append([0.9953488111495972, 0.99525005, 0.9953488111495972, 0.9953488111495972])
pi_rn.append([1.0, 1.0, 1.0, 1.0])
pi_rn.append([0.9976744055747986, 0.9976233, 0.9976744055747986, 0.9976744055747986])
pi_rn.append([1.0, 1.0, 1.0, 1.0])
pi_rn.append([0.9953488111495972, 0.99525005, 0.9953488111495972, 0.9953488111495972])

pi_rn_acc = []
pi_rn_prec = []
pi_rn_rec = []
pi_rn_f1 = []
for solution in pi_rn:
    pi_rn_acc.append(solution[0])
    pi_rn_prec.append(solution[1])
    pi_rn_rec.append(solution[2])
    pi_rn_f1.append(solution[3])

print("PI-RN\n")
print(f"Best acc: {np.max(pi_rn_acc)}, worst acc: {np.min(pi_rn_acc)}, mean acc: {np.mean(pi_rn_acc)}, std acc: {np.std(pi_rn_acc)}")
print(f"Best prec: {np.max(pi_rn_prec)}, worst prec: {np.min(pi_rn_prec)}, mean prec: {np.mean(pi_rn_prec)}, std prec: {np.std(pi_rn_prec)}")
print(f"Best rec: {np.max(pi_rn_rec)}, worst rec: {np.min(pi_rn_rec)}, mean rec: {np.mean(pi_rn_rec)}, std rec: {np.std(pi_rn_rec)}")
print(f"Best f1: {np.max(pi_rn_f1)}, worst f1: {np.min(pi_rn_f1)}, mean f1: {np.mean(pi_rn_f1)}, std f1: {np.std(pi_rn_f1)}\n\n")

#PI-XC

pi_xc = []

pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([0.9976744055747986, 0.9976233, 0.9976744055747986, 0.9976744055747986])
pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([0.9976744055747986, 0.9976233, 0.9976744055747986, 0.9976744055747986])
pi_xc.append([0.9976744055747986, 0.9976233, 0.9976744055747986, 0.9976744055747986])
pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([0.9953488111495972, 0.99525005, 0.9953488111495972, 0.9953488111495972])
pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([0.9953488111495972, 0.9952365, 0.9953488111495972, 0.9953488111495972])
pi_xc.append([0.9976744055747986, 0.9976233, 0.9976744055747986, 0.9976744055747986])
pi_xc.append([0.9976744055747986, 0.9976233, 0.9976744055747986, 0.9976744055747986])
pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([0.9930232763290405, 0.9928496, 0.9930232763290405, 0.9930232763290405])
pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([1.0, 1.0, 1.0, 1.0])
pi_xc.append([1.0, 1.0, 1.0, 1.0])

pi_xc_acc = []
pi_xc_prec = []
pi_xc_rec = []
pi_xc_f1 = []
for solution in pi_xc:
    pi_xc_acc.append(solution[0])
    pi_xc_prec.append(solution[1])
    pi_xc_rec.append(solution[2])
    pi_xc_f1.append(solution[3])

print("PI-XC\n")
print(f"Best acc: {np.max(pi_xc_acc)}, worst acc: {np.min(pi_xc_acc)}, mean acc: {np.mean(pi_xc_acc)}, std acc: {np.std(pi_xc_acc)}")
print(f"Best prec: {np.max(pi_xc_prec)}, worst prec: {np.min(pi_xc_prec)}, mean prec: {np.mean(pi_xc_prec)}, std prec: {np.std(pi_xc_prec)}")
print(f"Best rec: {np.max(pi_xc_rec)}, worst rec: {np.min(pi_xc_rec)}, mean rec: {np.mean(pi_xc_rec)}, std rec: {np.std(pi_xc_rec)}")
print(f"Best f1: {np.max(pi_xc_f1)}, worst f1: {np.min(pi_xc_f1)}, mean f1: {np.mean(pi_xc_f1)}, std f1: {np.std(pi_xc_f1)}\n\n")

#D0-RN

d0_rn = []

d0_rn.append([0.9966740608215332, 0.99623966, 0.9977728128433228, 0.9933481216430664])
d0_rn.append([0.9955654144287109, 0.9945987, 0.9966517686843872, 0.9900221824645996])
d0_rn.append([0.9977827072143555, 0.9981472, 0.9977728128433228, 0.9933481216430664])
d0_rn.append([0.9955654144287109, 0.9955753, 0.996662974357605, 0.9933481216430664])
d0_rn.append([0.9922394752502441, 0.99028015, 0.9955307245254517, 0.9878048896789551])
d0_rn.append([0.9966740608215332, 0.9970616, 0.9966592192649841, 0.9922394752502441])

d0_rn_acc = []
d0_rn_prec = []
d0_rn_rec = []
d0_rn_f1 = []
for solution in d0_rn:
    d0_rn_acc.append(solution[0])
    d0_rn_prec.append(solution[1])
    d0_rn_rec.append(solution[2])
    d0_rn_f1.append(solution[3])

print("D0-RN\n")
print(f"Best acc: {np.max(d0_rn_acc)}, worst acc: {np.min(d0_rn_acc)}, mean acc: {np.mean(d0_rn_acc)}, std acc: {np.std(d0_rn_acc)}")
print(f"Best prec: {np.max(d0_rn_prec)}, worst prec: {np.min(d0_rn_prec)}, mean prec: {np.mean(d0_rn_prec)}, std prec: {np.std(d0_rn_prec)}")
print(f"Best rec: {np.max(d0_rn_rec)}, worst rec: {np.min(d0_rn_rec)}, mean rec: {np.mean(d0_rn_rec)}, std rec: {np.std(d0_rn_rec)}")
print(f"Best f1: {np.max(d0_rn_f1)}, worst f1: {np.min(d0_rn_f1)}, mean f1: {np.mean(d0_rn_f1)}, std f1: {np.std(d0_rn_f1)}\n\n")

#D0-XC

d0_xc = []

d0_xc.append([0.9988913536071777, 0.99909097, 0.9988864064216614, 0.9944567680358887])
d0_xc.append([0.9911308288574219, 0.9892669, 0.9933110475540161, 0.9878048896789551])
d0_xc.append([0.9911308288574219, 0.98939735, 0.9966254234313965, 0.9822616577148438])
d0_xc.append([0.9933481216430664, 0.99204713, 0.9955456852912903, 0.9911308288574219])
d0_xc.append([0.9988913536071777, 0.99909097, 0.9988802075386047, 0.9889135360717773])
d0_xc.append([0.9933481216430664, 0.991738, 0.9955456852912903, 0.9911308288574219])

d0_xc_acc = []
d0_xc_prec = []
d0_xc_rec = []
d0_xc_f1 = []
for solution in d0_xc:
    d0_xc_acc.append(solution[0])
    d0_xc_prec.append(solution[1])
    d0_xc_rec.append(solution[2])
    d0_xc_f1.append(solution[3])

print("D0-XC\n")
print(f"Best acc: {np.max(d0_xc_acc)}, worst acc: {np.min(d0_xc_acc)}, mean acc: {np.mean(d0_xc_acc)}, std acc: {np.std(d0_xc_acc)}")
print(f"Best prec: {np.max(d0_xc_prec)}, worst prec: {np.min(d0_xc_prec)}, mean prec: {np.mean(d0_xc_prec)}, std prec: {np.std(d0_xc_prec)}")
print(f"Best rec: {np.max(d0_xc_rec)}, worst rec: {np.min(d0_xc_rec)}, mean rec: {np.mean(d0_xc_rec)}, std rec: {np.std(d0_xc_rec)}")
print(f"Best f1: {np.max(d0_xc_f1)}, worst f1: {np.min(d0_xc_f1)}, mean f1: {np.mean(d0_xc_f1)}, std f1: {np.std(d0_xc_f1)}\n\n")