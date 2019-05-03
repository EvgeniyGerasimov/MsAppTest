from data.methods import Methods
from data import request_body
from  jsonschema import validate
from data.JSON_Shemas import promotion_author_tool_shema, promotion_feature_strip_shema, promotion_top_block_shema


class TestPromotion:
    def test_promotion_top_block(self):
        response = Methods.post('/promotion/top-block/', request_body.TOP_BLOCK, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=promotion_top_block_shema.PROMOTION_TOP_BLOCK_SHEMA)

    def test_promotion_feature_strip(self):
        response = Methods.post('/promotion/feature-strip/', request_body.FEATURE_STRIP, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=promotion_feature_strip_shema.PROMOTION_FEATURE_STRIP_SHEMA)

    def test_promotion_author_tool(self):
        response = Methods.post('/promotion/author-tool/', request_body.AUTHOR_TOOL, Methods.headers)
        assert 200 == response.status_code
        validate(instance=response.json(), schema=promotion_author_tool_shema.PROMOTION_AUTHOR_TOOL)
