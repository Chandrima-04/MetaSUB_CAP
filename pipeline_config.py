from moduleultra.pipeline_config_utils import *
from os.path import join


def scriptDir(fpath):
    dname = fromPipelineDir('/scripts/')
    return dname + fpath


def pmegaDB(operand):
    cmd = 'packagemega database {}'.format(operand)
    return resolveCmd(cmd)


def which(tool):
    cmd = 'which {}'.format(tool)
    return resolveCmd(cmd)


config = {
    'align_to_sa_n315': {
        'threads': 6,
        'time': 10,
        'ram': 10,
        'db': {
            'bt2': pmegaDB('staph_aureus_n315.bt2.prefix')
        }
    },
    'alpha_diversity_stats': {
        'script': scriptDir('alpha_diversity_stats.py')
    },
    'microbe_directory_annotate': {
        'script': scriptDir('microbe_directory_annotate.py'),
        'db': scriptDir('microbe-directory.csv')
    },
    'beta_diversity_stats': {
        'script': scriptDir('beta_diversity_stats.py')
    },
    'read_classification_proportions': {
        'script': scriptDir('count_classified_reads.py')
    },
    'read_stats': {
        'script': scriptDir('read_stats.py')
    },
    'metaphlan2_taxonomy_profiling': {
        'exc': {
            'filepath': which('metaphlan2.py'),
            'version': resolveCmd('metaphlan2.py --version 2>&1')
        },
        'threads': 2,
        'time': 2,
        'ram': 5
    },
    'midas_single_samples': {
        'time': 4,
        'ram': 4,
        'threads': 6,
        'exc': {
            'filepath': which('run_midas.py')
        },
        'db': {
            'filepath': pmegaDB('midas.default_midas.0')
        }
    },
    'midas_merge_groups': {
        'exc': {
            'filepath': which('merge_midas.py')
        }
    },
    'kraken_taxonomy_profiling': {
        'exc': {
            'filepath': which('kraken'),
            'version': resolveCmd('kraken --version | tr "\n"  " "')
        },
        'db': {
            'filepath': pmegaDB('minikraken.kraken-db.dir')
        },
        'mpa_exc': {
            'filepath': which('kraken-mpa-report'),
            'version': resolveCmd('kraken-mpa-report --version | tr "\n"  " "')
        },
        'threads': 2,
        'time': 2,
        'ram': 5
    },
    'microbe_census_group_summary': {
        'script': scriptDir('summarize_microbe_census.py')
    },
    'kraken_group_summary': {
        'script': scriptDir('summarize_kraken.py')
    },
    'normalized_kraken_taxonomy': {
        'script': scriptDir('average_genome_size_normalization.py')
    },
    'mash': {
        'exc': {
            'filepath': which('mash'),
            'version': resolveCmd('mash --version')
        }
    },
    'humann2_functional_profiling': {
        'exc': {
            'filepath': which('humann2'),
            'version': resolveCmd('humann2 --version 2>&1')
        },
        'db': {
            'filepath': pmegaDB('uniref90.dmnd.0')
        },
        'dmnd': {
            'time': 10,
            'ram': 6,
            'threads': 10,
            'block_size': 6
        },
        'threads': 1,
        'time': 1,
        'ram': 32
    },
    'microbe_census': {
        'threads': 6,
        'time': 4,
        'ram': 10,
        'exc': {
            'filepath': which('run_microbe_census.py'),
            'version': resolveCmd('run_microbe_census.py --version 2>&1')
        }
    },
    'shortbred': {
        'exc': {
            'filepath': which('shortbred_quantify.py'),
            'version': ''
        }
    },
    'shortbred_amr_profiling': {
        'ref': {
            'filepath': pmegaDB('card.sbred.0')
        },
        'threads': 2,
        'time': 2,
        'ram': 5
    },
    'resistome_amrs': {
        'threads': 4,
        'thresh': 80,
        'exc': {
            'filepath': which('resistome')
        },
        'db': {
            'bt2': pmegaDB('megares.bt2.prefix'),
            'fasta': pmegaDB('megares.fasta.0'),
            'annotations': pmegaDB('megares.csv.0')
        },
        'bt2_time': 2,
        'bt2_ram': 10
    },
    'bt2': {
        'exc': {
            'filepath': which('bowtie2'),
            'version': resolveCmd('bowtie2 --version')
        }
    },
    'diamond': {
        'exc': {
            'filepath': which('diamond'),
            'version': resolveCmd('diamond --version')
        }
    },
    'filter_macrobial_dna': {
        'db': {
            'filepath': pmegaDB('common_macrobial.bt2.prefix')
        },
        'threads': 6,
        'time': 10,
        'ram': 10
    },
    'filter_human_dna': {
        'db': {
            'filepath': pmegaDB('hg38_ucsc.bt2.prefix')
        },
        'threads': 6,
        'time': 10,
        'ram': 10
    },
    'align_to_methyltransferases': {
        'threads': 6,
        'time': 10,
        'ram': 10,
        'db': {
            'bt2': ''
        }
    },
    'align_to_amr_genes': {
        'threads': 6,
        'time': 10,
        'ram': 10,
        'card_amrs': {
            'bt2': '/athena/masonlab/scratch/users/dcd3001/Refs/CAP_databases/abr_genes/CARD/ARmeta-genes.nt2'
        }
    },
    'samtools': {
        'filepath': which('samtools')
    },
    'humann2_normalize_genes': {
        'script': scriptDir('normalize_genes.py')
    },
    'python2': which('python2'),
    'adapter_removal': {
        'time': 2,
        'threads': 6,
        'ram': 10,
        'exc': {
            'filepath': which('AdapterRemoval'),
            'version': resolveCmd('AdapterRemoval --version 2>&1')
        }
    }
}