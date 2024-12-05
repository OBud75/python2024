from textblob import TextBlob

report = """This Q4 was a record-breaking Holiday shopping season and closed out a robust 2023 for Amazon,” said Andy Jassy, Amazon
CEO. “While we made meaningful revenue, operating income, and free cash flow progress, what we're most pleased with is the
continued invention and customer experience improvements across our businesses. The regionalization of our U.S. fulfillment
network led to our fastest-ever delivery speeds for Prime members while also lowering our cost to serve; AWS's continued
long-term focus on customers and feature delivery, coupled with new genAI capabilities like Bedrock, Q, and Trainium have
resonated with customers and are starting to be reflected in our overall results; our Advertising services continue to improve
and drive positive results; our newer businesses are progressing nicely, and along with our more established businesses,
collectively making customers' lives easier and better every day. As we enter 2024, our teams are delivering at a rapid clip, and
we have a lot in front of us to be excited about."""

text = TextBlob(text=report)
print(text.sentiment)
