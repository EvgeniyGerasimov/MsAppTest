from data.methods import Methods
from data import body


class TestPromotion:
    def test_promotion_top_block(self):
        response = Methods.post('/promotion/top-block/', body.TOP_BLOCK, Methods.headers)
        assert 200 == response.status_code

    def test_promotion_feature_strip(self):
        response = Methods.post('/promotion/feature-strip/', body.FEATURE_STRIP, Methods.headers)
        assert 200 == response.status_code

    def test_promotion_author_tool(self):
        response = Methods.post('/promotion/top-block/', body.AUTHOR_TOOL, Methods.headers)
        assert 200 == response.status_code
