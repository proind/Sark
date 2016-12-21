class CollectionsWrapper(object):
    def __getitem__(self, slice_index):
        """
        syntethic sugar to allow getting a list of Lines by slicing ,
        as you would with a list
        :param slice_index: either a slice or an int
        :return: list of Lines
        """
        if isinstance(slice_index, slice):
            return list(self.generator(slice_index.start, slice_index.stop))
        elif isinstance(slice_index, int):
            return list(self.generator(slice_index, slice_index))
        else:
            raise TypeError("Bad input - use only ints or slices")

    def __call__(self, *args, **kwargs):
        return self.generator(*args, **kwargs)

    @staticmethod
    def generator(start=None, end=None):
        raise NotImplementedError("Inherit CollectionsWrapper and implement this function")