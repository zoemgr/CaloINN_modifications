
import h5py
import numpy as np
import os

original_file = "/pbs/home/z/zriche/CaloINN/data/dataset_1_pions_1_missing.hdf5"

# with h5py.File(input_file, 'r') as f:
#     print("Clés disponibles dans le fichier HDF5 :")
#     for key in f.keys():
#         print(f"{key} --> shape: {f[key].shape}, dtype: {f[key].dtype}")


output_dir = "/pbs/home/z/zriche/CaloINN/data/filtered"
os.makedirs(output_dir, exist_ok=True)

values_to_remove = [2097152.0]
#values_to_remove = [1024.0, 16384.0, 1048576.0]

for value in values_to_remove:
    with h5py.File(original_file, 'r') as f_in:
        incident_energies = f_in['incident_energies'][()]
        showers = f_in['showers'][()]
        index_to_remove = np.where(incident_energies == value)[0]
        filtered_energies = np.delete(incident_energies, index_to_remove, axis=0)
        filtered_showers = np.delete(showers, index_to_remove, axis=0)

        output_file = os.path.join(output_dir, f"dataset_1_pions_no_{int(value)}.hdf5")
        with h5py.File(output_file, 'w') as f_out:
            f_out.create_dataset('incident_energies', data=filtered_energies)
            f_out.create_dataset('showers', data=filtered_showers)
        print(f" Fichier créé ")

