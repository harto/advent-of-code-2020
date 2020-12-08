with open('inputs/08') as f:
    orig_prog = []
    for line in f:
        cmd, arg = line.strip().split(' ')
        orig_prog.append((cmd, int(arg)))

def run_prog(prog):
    seen_lines = set()
    acc = 0
    i = 0
    while i < len(prog):
        if i in seen_lines:
            return acc, False
        seen_lines.add(i)
        cmd, arg = prog[i]
        if cmd == 'acc':
            acc += arg
            i += 1
        elif cmd == 'jmp':
            i += arg
        elif cmd == 'nop':
            i += 1
        else:
            raise cmd
    return acc, True

acc, _ = run_prog(orig_prog)
print(acc)

for i, line in enumerate(orig_prog):
    if line[0] not in ('jmp', 'nop'):
        continue
    modified_line = ('jmp' if line[0] == 'nop' else 'nop', line[1])
    modified_prog = orig_prog[:i] + [modified_line] + orig_prog[i+1:]
    acc, finished = run_prog(modified_prog)
    if finished:
        print(acc)
        break
