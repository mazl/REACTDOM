require "rubygems"
require "rspec"
require "watir-webdriver"

describe "google.com" do 
  let(:browser) { @browser ||= Watir::Browser.new :ie } 
  before { browser.goto "http://www.baidu.com" } 
  after { browser.close }

  it "should search for watir" do 
    browser.text_field(:name => "q").set "watir"
    browser.button.click 
    browser.div(:id => "resultStats").wait_until_present
    browser.title.should == "watir - Google Search"
  end
end