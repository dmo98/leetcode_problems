class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            'Jan':'01',
            'Feb':'02',
            'Mar':'03',
            'Apr':'04',
            'May':'05',
            'Jun':'06',
            'Jul':'07',
            'Aug':'08',
            'Sep':'09',
            'Oct':'10',
            'Nov':'11',
            'Dec':'12'
        }
        
        day, month, year = date.split(" ")
        
        month = months[month]
        day = day[:-2]
        if len(day) == 1:
            day = '0'+day
        
        reformat_date = [year, month, day]
        return "-".join(reformat_date)
        