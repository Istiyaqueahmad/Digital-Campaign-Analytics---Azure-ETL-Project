
CREATE TABLE dbo.CampaignPerformance (
  CampaignID INT PRIMARY KEY,
  CampaignName NVARCHAR(100),
  Impressions INT,
  Clicks INT,
  Conversions INT,
  Spend DECIMAL(18,2),
  Date DATE
);
