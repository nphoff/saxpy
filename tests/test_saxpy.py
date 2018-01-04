from saxpy import SAX
import numpy as np

class TestSAX(object):
    def setUp(self):
        # All tests will be run with 6 letter words
        # and 5 letter alphabet
        self.sax = SAX(6, 5, 1e-6)

    def test_to_letter_rep(self):
        arr = [7,1,4,4,4,4]
        (letters, indices) = self.sax.to_letter_rep(arr)
        assert letters == 'eacccc'

    def test_to_letter_rep_missing(self):
        arr = [7,1,4,4,np.nan,4]
        (letters, indices) = self.sax.to_letter_rep(arr)
        assert letters == 'eacc-c'

    def test_long_to_letter_rep(self):
        long_arr = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,6,6,6,6,10,100]
        (letters, indices) = self.sax.to_letter_rep(long_arr)
        assert letters == 'bbbbce'

    def test_long_to_letter_rep_missing(self):
        long_arr = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,np.nan,1,1,6,6,6,6,10,100]
        (letters, indices) = self.sax.to_letter_rep(long_arr)
        assert letters == 'bbb-ce'

    def test_compare_strings(self):
        base_string = 'aaabbc'
        similar_string = 'aabbbc'
        dissimilar_string = 'ccddbc'
        similar_score = self.sax.compare_strings(base_string, similar_string)
        dissimilar_score = self.sax.compare_strings(base_string, dissimilar_string)
        assert similar_score < dissimilar_score

    def test_compare_strings_missing(self):
        assert self.sax.compare_strings('a-b-c-', 'b-c-d-') == 0

    def test_normalize_missing(self):
        # two arrays which should normalize to the same result
        # except one should contain a nan value in place of the input nan value
        incomplete_arr_res = self.sax.normalize([1,0,0,0,0,1,np.nan])
        complete_arr_res = self.sax.normalize([1,0,0,0,0,1])
        assert np.array_equal(incomplete_arr_res[:-1], complete_arr_res)
        assert np.isnan(incomplete_arr_res[-1])