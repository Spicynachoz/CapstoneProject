package org.turntotech.notification;

import android.content.Context;
import android.graphics.Color;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Adapter;
import android.widget.ArrayAdapter;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.ArrayList;


public class MyCustomBaseAdapter extends BaseAdapter{
    private static ArrayList<String[]> searchArrayList;
    private String month;
    private String team;
    private LayoutInflater mInflater;

    public MyCustomBaseAdapter(Context context, ArrayList<String[]> results,String Smonth,String Steam) {
        searchArrayList = results;
        month=Smonth;
        team=Steam;

        mInflater = LayoutInflater.from(context);
    }

    public int getCount() {
        return searchArrayList.size();
    }

    public Object getItem(int pos1) {
        return searchArrayList.get(pos1);
    }

    public long getItemId(int pos1) {
        return((pos1) );
    }

    public View getView(int position, View convertView, ViewGroup parent) {
        /*for (int i = 0; i <searchArrayList.size(); i++) {
            if( ( searchArrayList.get(i)[0].contains(month.substring(0,2)) ) && ( ((searchArrayList.get(i)[3]).equals(team))||((searchArrayList.get(i)[0]).equals(team)) ) ) {

                searchArrayList.remove(i);
            }
        }*/
        ViewHolder holder;
        if (convertView == null) {
            convertView = mInflater.inflate(R.layout.custom_row_view, null);
            holder = new ViewHolder();
            holder.txtDate = (TextView) convertView.findViewById(R.id.date);
            holder.txtTime = (TextView) convertView.findViewById(R.id.time);
            holder.txtHome = (TextView) convertView.findViewById(R.id.home);
            holder.txtAway = (TextView) convertView.findViewById(R.id.away);
            holder.txtHscore = (TextView) convertView.findViewById(R.id.hscore);
            holder.txtAscore = (TextView) convertView.findViewById(R.id.ascore);
            convertView.setTag(holder);
        } else {
            holder = (ViewHolder) convertView.getTag();
        }
       // if( ( searchArrayList.get(position)[0].contains(month.substring(0,2)) ) && ( ((searchArrayList.get(position)[3]).equals(team))||((searchArrayList.get(position)[0]).equals(team)) ) ){


            holder.txtDate.setText(searchArrayList.get(position)[0]);
            holder.txtTime.setText(searchArrayList.get(position)[1]);
            holder.txtHome.setText(searchArrayList.get(position)[5]);
            holder.txtAway.setText(searchArrayList.get(position)[3]);
            holder.txtHscore.setText(searchArrayList.get(position)[6]);
            holder.txtAscore.setText(searchArrayList.get(position)[4]);

            return convertView;
        //}




    }

    static class ViewHolder {
        TextView txtDate;
        TextView txtTime;
        TextView txtHome;
        TextView txtAway;
        TextView txtHscore;
        TextView txtAscore;
    }
}