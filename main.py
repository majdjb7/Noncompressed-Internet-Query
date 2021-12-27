from NonCompressedIndexWriter import NonCompressedIndexWriter
from IndexReader import IndexReader


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   # c = 'HereText'
  #  dxW = NonCompressedIndexWriter('100.txt', c)
    # dxW.removeIndex(c)

    DIR = "prj_index"

    # create an instance of the index writer class

  ######  idxW = NonCompressedIndexWriter(input_FILE, DIR)
    idxW = NonCompressedIndexWriter('1000.txt', DIR)

   # create an instance of the index reader class

    idxR = IndexReader(DIR)

    REVIEW_ID = 18

    TOKEN = "Covid19"
    TOKEN2 = "products"
    TOKEN3 = "food"

    PRODUCT_ID = "B0019CW0HE"
    PRODUCT_ID2 = "B001EO5QW8"
    PRODUCT_ID4 = "B006F2NYI2"
    PRODUCT_ID3 = "ZMNKSI093"

# use the index reader to query the system
    print("Product ID for the review")
    print(idxR.getProductId(REVIEW_ID))

    print("Review Score")
    print(idxR.getReviewScore(REVIEW_ID))

    print("Numerator:")
    print(idxR.getReviewHelpfulnessNumerator(REVIEW_ID))

    print("Denominator:")
    print(idxR.getReviewHelpfulnessDenominator(REVIEW_ID))



    print("Review Length:")
    print(idxR.getReviewLength(REVIEW_ID))

    print("Token Frequency for COVID19:")
    print(idxR.getTokenFrequency(TOKEN))

    print("Token Frequency for products:")
    print(idxR.getTokenFrequency(TOKEN2))
    print("TOKEN collection frequency for food:")
    print(idxR.getTokenCollectionFrequency(TOKEN3))
    print("TOKEN collection frequency for not COVID19:")
    print(idxR.getTokenCollectionFrequency(TOKEN))

    print("Series (work) - products")
    print(idxR.getReviewsWithToken(TOKEN2))
    print("Series (work) - food")
    print(idxR.getReviewsWithToken(TOKEN3))
    print("Series (not work) - COVID19")
    print(idxR.getReviewsWithToken(TOKEN))

    print("NUM OF REVIEWS:")
    print(idxR.getNumberOfReviews())

    print("TOTAL TOKEN SIZE:")
    print(idxR.getTokenSizeOfReviews())

    print("REVIEWS for p ID (works")
    print(idxR.getProductReviews(PRODUCT_ID))
    print(idxR.getProductReviews(PRODUCT_ID2))
    print(idxR.getProductReviews(PRODUCT_ID4))
    print("REVIEWS for p ID (not works")
    print(idxR.getProductReviews(PRODUCT_ID3))

    idxW.removeIndex(DIR)









