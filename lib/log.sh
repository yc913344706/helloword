#!/bin/bash

case $LOG_LEVEL in
        error)
               log_level_num=4
               ;;
        warn)
               log_level_num=3
               ;;
        info)
               log_level_num=2
               ;;
        debug)
               log_level_num=1
               ;;
        all)
               log_level_num=0
               ;;
        *)
               log_level_num=2
               ;;
esac

die()
{
    log_error "$*"
    exit 1
}

log()
{
    log_info "$*"
}

log_error()
{
        [ ${log_level_num} -le 4 ] || return 0
        date +"[ERROR] %F %T ${0##*/}: $*" >&2
}

log_warn()
{
        [ ${log_level_num} -le 3 ] || return 0
        date +"[WARN] %F %T ${0##*/}: $*" >&2
}

log_info()
{
        [ ${log_level_num} -le 2 ] || return 0
        date +"[INFO] %F %T ${0##*/}: $*"
}

log_debug()
{
        [ ${log_level_num} -le 1 ] || return 0
        date +"[DEBUG] %F %T ${0##*/}: $*"
}
