from eAE.eAE import eAE

def main():
    # Setting up the connection to interface
    ip = "interfaceeae.doc.ic.ac.uk"
    port = 443
    eae = eAE(ip, port)

    # Testing if the interface is Alive
    is_alive = eae.is_eae_alive()
    if is_alive != 200:
        raise Exception("!!!")

    # Get all jobs
    args = ['--data_dir data/eeg_fpz_cz --output_dir results --n_folds 20 --fold_idx {} --pretrain_epochs 100 --finetune_epochs 200'.format(fold_idx) for fold_idx in range(20)]

    # We submit a dummy job
    parameters_set = "\n".join(args)
    cluster = "gpu"
    computation_type = "GPU"
    main_file = "train.py"
    data_files = ['deepsleep', 'tensorlayer', 'data/eeg_fpz_cz']
    host_ip = "dsigpu2.ict-doc.ic.ac.uk"
    ssh_port = "22222"
    job = eae.submit_jobs(parameters_set, cluster, computation_type, main_file, data_files, host_ip, ssh_port)
    print(job)


if __name__ == "__main__":
    main()