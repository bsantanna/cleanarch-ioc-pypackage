from app.core.config import Settings

class TestSettings:
    def test_schema_list(self):
        settings = Settings(SCHEMAS="schema1, schema2, public")
        result = settings.schema_list
        assert result == ["schema1", "schema2", "public"], "It should return a list of correct schemas"

        settings = Settings(SCHEMAS=" schema1 , schema2 , public ")
        result = settings.schema_list
        assert result == ["schema1", "schema2", "public"], "It should ignore extra spaces in schemas"

    def test_schema_list_without_public(self):
        settings = Settings(SCHEMAS="schema1, schema2, public, public_schema")
        result = settings.schema_list_without_public
        assert result == ["schema1", "schema2"], "It should exclude 'public' and 'public_schema' from the list"

        settings = Settings(SCHEMAS=" schema1 , schema2 , public , public_schema ")
        result = settings.schema_list_without_public
        assert result == ["schema1", "schema2"], "It should ignore extra spaces and exclude 'public' and 'public_schema'"

        settings = Settings(SCHEMAS="public, public_schema")
        result = settings.schema_list_without_public
        assert result == [], "It should return an empty list when there are only public schemas"
