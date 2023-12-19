class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:
        def nbrs(xs, k=1):
            return product(*(range(x - k, x + k + 1) for x in xs))
        
        def in_bound(xs, lb, rb):
            return all(map(le, lb, xs)) and all(map(lt, xs, rb))
        
        def val(m, x):
            return reduce(getitem, x, m)
        
        lb = (0, 0)
        rb = (len(img), len(img[0]))
        foo = lambda x: floor(mean(val(img, nbr) for nbr in nbrs(x) if in_bound(nbr, lb, rb)))

        s_img = [[0] * rb[1] for _ in range(rb[0])]
        for i, j in product(range(rb[0]), range(rb[1])):
            s_img[i][j] = foo((i, j))
        return s_img

