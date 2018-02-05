from subprocess import CalledProcessError

from src.exif import Exif


def test_exif_reads_valid_file():
    exif = Exif("files/input/in_exif.jpg")
    assert exif.data()['CreateDate'] == '2017:01:01 01:01:01'

def test_exif_handles_exception(mocker):
    mocker.patch('subprocess.check_output', side_effect=CalledProcessError(2, 'cmd'))
    exif = Exif("not-existing.jpg")
    assert exif.data() == None