#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

class Solution {
public:
    struct less_than_lastDay
    {
        inline bool operator() (const vector<int>& v1, const vector<int>& v2)
        {
            return (v1[1] < v2[1]);
        }
    };
    
    int scheduleCourse(vector<vector<int> >& courses) {
        priority_queue<int> selected_courses_pq;  // priority queue sorted by duration
        int accumulator = 0;

        // sort by lastDay (EDF - Earliest Deadline First Scheduling)
        sort(courses.begin(), courses.end(), less_than_lastDay());

        // add to accumulator unitl it reaches the dealine
        for(int runner=0; runner < courses.size(); runner++) {
          accumulator += courses[runner][0];
          selected_courses_pq.push(courses[runner][0]);

          if(accumulator > courses[runner][1]) {
            // roll back accumulator and pop the course with the largest duration
            accumulator -= selected_courses_pq.top();
            selected_courses_pq.pop();  // pq pop
          }
        }
        return selected_courses_pq.size();
    }
};

int main() {
  Solution *s = new Solution();
  vector<vector<int> > courses {
                          {2,5},
                          {2,19},
                          {1,8},
                          {1,3}
                        };
  printf("%d\n", s->scheduleCourse(courses));

  return 0;
}
