import omni.graph.core as og

# inputs: baselink_com(float[3]), back_com(float[3]), sacrum_com(float[3]),
#         l_hip_com(float[3]), r_hip_com(float[3]),
#         l_thigh_com(float[3]), r_thigh_com(float[3]),
#         l_calf_com(float[3]),  r_calf_com(float[3]),
#         l_ankle_com(float[3]), r_ankle_com(float[3]),
#         l_foot_com(float[3]),  r_foot_com(float[3])
# outputs: com_array(float[])

def compute(db: og.Database):
    parts = [
        db.inputs.baselink_com,
        db.inputs.back_com,
        db.inputs.sacrum_com,
        db.inputs.l_hip_com,
        db.inputs.r_hip_com,
        db.inputs.l_thigh_com,
        db.inputs.r_thigh_com,
        db.inputs.l_calf_com,
        db.inputs.r_calf_com,
        db.inputs.l_ankle_com,
        db.inputs.r_ankle_com,
        db.inputs.l_foot_com,
        db.inputs.r_foot_com,
    ]

    arr = []
    for p in parts:
        if p is not None and len(p) == 3:
            arr.extend([float(p[0]), float(p[1]), float(p[2])])
        else:
            arr.extend([0.0, 0.0, 0.0])

    db.outputs.com_array = arr
    return True