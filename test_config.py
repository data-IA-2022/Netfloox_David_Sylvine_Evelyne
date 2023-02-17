import pytest, os.path
import utils


def test_config_file():
    '''
    Vérifie que le fichier config existe bien...
    :return: None
    '''
    assert os.path.exists(utils.CONFIG_FILE)

def test_config_content():
    '''
    Vérifie le contenu de config.yaml
    :return: None
    '''
    cfg = utils.get_config()
    assert 'host' in cfg


def test_engine():
    engine = utils.get_engine()
    assert engine is not None