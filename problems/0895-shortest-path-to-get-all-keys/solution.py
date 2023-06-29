class Solution:
    def shortestPathAllKeys(self, grid: list[str]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

        in_bounds = lambda i, j: 0 <= i < m and 0 <= j < n
        nbrs = lambda i, j: ((i + di, j + dj) for di, dj in dirs)

        starfilter = lambda f, xs: filter(lambda args: f(*args), xs)
        starfilterfalse = lambda f, xs: filterfalse(lambda args: f(*args), xs)

        is_x = lambda val, x: val in x
        is_empty = partial(is_x, x='.')
        is_wall = partial(is_x, x='#')
        is_start = partial(is_x, x='@')
        is_key = partial(is_x, x='abcdef')
        is_lock = partial(is_x, x='ABCDEF')

        matrix2d_get = lambda i, j, mtx: mtx[i][j]
        get = partial(matrix2d_get, mtx=grid)

        k = sum(map(is_key, chain.from_iterable(grid)))
        start = next(filter(lambda ij: is_start(get(*ij)), product(range(m), range(n))))
        
        frontier = deque([(start, 0, frozenset())])
        seen = {(indices, keys) for indices, d, keys in frontier}

        while frontier:
            (i, j), d, keys = frontier.popleft()

            nbrs_ = starfilter(in_bounds, nbrs(i, j)) # Keep only inbound nbrs.
            nbrs_ = filter(lambda nbr: (nbr, keys) not in seen, nbrs_) # Keep only nbr not seen with same keys.

            nbr_and_vals = map(lambda nbr: (nbr, get(*nbr)), nbrs_) # Pair up nbr and containing value.
            nbr_and_vals = starfilterfalse(lambda _, val: is_wall(val), nbr_and_vals) # Remove nbr with WALL as value.
            nbr_and_vals = starfilterfalse(lambda _, val: is_lock(val) and val.lower() not in keys, nbr_and_vals) # Remove nbr with LOCK to which we don't have key yet, as value. 

            for nbr, val in nbr_and_vals:
                new_d, new_keys = d + 1, (keys | {val} if is_key(val) else keys)
                if len(new_keys) == k: return new_d

                frontier.append((nbr, new_d, new_keys))
                seen.add((nbr, new_keys))
        
        return -1

