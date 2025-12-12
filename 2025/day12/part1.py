from sys import stdin
from functools import cache

lines = [line.rstrip('\n') for line in stdin if line.strip()]

shapes: dict[int, list[str]] = {}
regions: list[tuple[int, int, list[int]]] = []

i = 0
while i < len(lines) and lines[i][-1] == ':':
    idx_str, shape_lines = lines[i].split(':')[0], []
    i += 1
    while i < len(lines) and lines[i] and not lines[i][0].isdigit() and ':' not in lines[i]:
        shape_lines.append(lines[i])
        i += 1
    shapes[int(idx_str)] = shape_lines

while i < len(lines):
    if 'x' in lines[i]:
        size_part, region_info = lines[i].split(': ')
        w, h = sorted(map(int, size_part.split('x')))
        counts = list(map(int, region_info.split()))
        regions.append((w, h, counts))
    i += 1

def shape_to_coords(grid: list[str]) -> list[tuple[int, int]]:
    coords = []
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == '#':
                coords.append((r, c))
    return coords

def gen_transforms(coords: list[tuple[int, int]]):
    result: set[tuple[tuple[int, int], ...]] = set()

    def normalize(coords: list[tuple[int, int]]):
        minr = min(r for r, _ in coords)
        minc = min(c for _, c in coords)
        norm = tuple(sorted(((r - minr, c - minc) for r, c in coords)))
        return norm

    for reflect in (False, True):
        for rot in range(4):
            out = []
            for r, c in coords:
                c2 = -c if reflect else c
                rr, cc = r, c2
                for _ in range(rot):
                    rr, cc = cc, -rr
                out.append((rr, cc))
            result.add(normalize(out))
    return result

shapes_orients: dict[int, list[tuple[tuple[int, int], ...]]] = {}
for idx, grid in shapes.items():
    coords = shape_to_coords(grid)
    orients = gen_transforms(coords)
    shapes_orients[idx] = list(orients)

@cache
def gen_placements(w: int, h: int, s_idx: int):
    placements: list[tuple[int, ...]] = []
    placements_set = set()

    for orient in shapes_orients[s_idx]:
        maxr = max(r for r, _ in orient)
        maxc = max(c for _, c in orient)

        for base_r in range(0, h - maxr):
            for base_c in range(0, w - maxc):
                occ = []
                for (sr, sc) in orient:
                    rr = base_r + sr
                    cc = base_c + sc
                    occ.append(rr * w + cc)
                placement = tuple(sorted(occ))
                if placement not in placements_set:
                    placements_set.add(placement)
                    placements.append(placement)
    return placements

answer = 0
for w, h, needs in regions:
    total_cells_needed = 0
    for s_idx, count in enumerate(needs):
        if count == 0:
            continue
        area = len(shapes_orients[s_idx][0])
        total_cells_needed += area * count
    if total_cells_needed > w * h:
        continue

    placements: dict[int, list[tuple[int, ...]]] = {}
    for s_idx, count in enumerate(needs):
        if count == 0:
            placements[s_idx] = []
            continue
        pls = gen_placements(w, h, s_idx)
        placements[s_idx] = pls

    shape_order = [i for i, c in enumerate(needs) if c > 0]
    shape_order.sort(key=lambda s: (
        len(placements[s]), -len(shapes_orients[s][0])))

    occupied: set[int] = set()

    def place_shape(idx_shape: int) -> bool:
        if idx_shape >= len(shape_order):
            return True

        s = shape_order[idx_shape]
        need = needs[s]
        pls = placements[s]

        def place_k(k_remaining: int, start_index: int,
                    occ_local: set[int], chosen_indices: list[int]) -> bool:
            if k_remaining == 0:
                if place_shape(idx_shape + 1):
                    return True
                return False

            for i in range(start_index, len(pls) - k_remaining + 1):
                p = pls[i]
                if any(cell in occ_local for cell in p):
                    continue

                for cell in p:
                    occ_local.add(cell)
                chosen_indices.append(i)

                if place_k(k_remaining - 1, i + 1, occ_local, chosen_indices):
                    return True

                chosen_indices.pop()
                for cell in p:
                    occ_local.remove(cell)

            return False
        return place_k(need, 0, occupied, [])
    if place_shape(0):
        answer += 1

print(answer)
