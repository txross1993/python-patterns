'''
Cache data pulled from external sources to speed up testing
'''
import os
import pickle


def cached(cache_filename: str):
    '''
    A function that creates a decorator that will be used to cache
    the decorated functions output in a pickle filename of your choosing
    '''
    def decorator(fn):
        def wrapped(*args, **kwargs):
            # return cached results if exists
            if os.path.exists(cache_filename):
                with open(cache_filename, 'rb') as cachehandler:
                    print('using cached results to %s'.format(cache_filename))
                    return pickle.load(cachehandler)

            # cache the results if the cache didn't exist
            res = fn(*args, **kwargs)
            with open(cache_filename, 'wb') as cachehandler:
                print('saving results to cache file %s'.format(cache_filename))
                pickle.dump(res, cachehandler)

            return res

        return wrapped

    return decorator
