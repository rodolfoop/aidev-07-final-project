import unittest
from emotion_detection.emotion_detection import emotion_detector

class test_emotion_detection(unittest.TestCase):
    def test_emotion_detection(self):
        text1 = 'I am glad this happened'
        text2 = 'I am really mad about this'
        text3 = 'I feel disgusted just hearing about this'
        text4 = 'I am so sad about this'
        text5 = 'I am really afraid that this will happen'

        result1 = emotion_detector(text1)
        result2 = emotion_detector(text2)
        result3 = emotion_detector(text3)
        result4 = emotion_detector(text4)
        result5 = emotion_detector(text5)

        self.assertEqual(result1['dominant_emotion'], 'joy')
        self.assertEqual(result2['dominant_emotion'], 'anger')
        self.assertEqual(result3['dominant_emotion'], 'disgust')
        self.assertEqual(result4['dominant_emotion'], 'sadness')
        self.assertEqual(result5['dominant_emotion'], 'fear')

unittest.main()