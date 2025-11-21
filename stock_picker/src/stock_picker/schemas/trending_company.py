from pydantic import BaseModel, Field

class TrendingCompanySchema(BaseModel):
    name: str = Field(description="Company name")
    ticker: str = Field(description="Stock ticker symbol")
    reason: str = Field(description="Reason why the company is trending")


class TrendingCompaniesListSchema(BaseModel):
    companies: list[TrendingCompanySchema] = Field(
        description="List of trending companies")
    

class TrendingCompaniesResearchSchema(BaseModel):
    name: str = Field(description="Company name")
    market_position : str = Field(
        description="Current market position "
    )
    future_outlook : str = Field(
        description="Future outlook of the company"
    )
    investment_potential: str = Field(
        description="Investment potential of the company"
    )


class TrendingCompaniesResearchListSchema(BaseModel):
    research_list: list[TrendingCompaniesResearchSchema] = Field(
        description="List of researched trending companies"
    )
