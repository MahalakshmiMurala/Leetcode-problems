class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        title = title.split()
        st = []
        for i in title:
            if len(i)==1 or len(i)==2:
                st.append(i.lower())
            else:
                st.append(i.capitalize())
        return ' '.join(st)