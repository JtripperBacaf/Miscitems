import dis
import marshal

def disassemble_pyc(pyc_file):
    with open(pyc_file, 'rb') as f:
        # skip timestamp and magic num
        f.seek(12)
        # read byte code
        code = marshal.load(f)
        dis.dis(code)

# disassemble
disassemble_pyc('test.pyc')